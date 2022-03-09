#!/usr/bin/env python3
"""
Print storage information for every HDF5 dataset in a file.

Run "store_info.py --help" for information.
"""
from os import SEEK_SET, environ
import argparse
import json
from functools import partial
import typing
from hashlib import sha3_256
from uuid import uuid4
from urllib.parse import urlparse
import h5py
import s3fs


def storage_info(dset: h5py.Dataset, use_iter: bool = False) -> list:
    """Collect dataset storage information"""

    def chunk_info(chunk_stor, stinfo):
        stinfo.append(chunk_stor)

    if dset.shape is None:
        # Empty (null) dataset...
        return list()

    dsid = dset.id
    if dset.chunks is None:
        # Contiguous dataset...
        if dsid.get_offset() is None:
            return list()
        else:
            return [h5py.h5d.StoreInfo((0,) * len(dset.shape),
                                       0,
                                       dsid.get_offset(),
                                       dsid.get_storage_size())]
    else:
        # Chunked dataset...
        num_chunks = dsid.get_num_chunks()
        if num_chunks == 0:
            return list()

        # Go over all the chunks...
        stinfo = list()
        if use_iter:
            dset.visit_chunks(partial(chunk_info, stinfo=stinfo))
        else:
            for index in range(num_chunks):
                stinfo.append(dsid.get_chunk_info(index))

        return stinfo


def get_cksum(fobj: typing.BinaryIO, offset: int, blen: int):
    if fobj:
        fobj.seek(offset, SEEK_SET)
        byte_stream = fobj.read(blen)
        if len(byte_stream) != blen:
            raise IOError(
                'Read %d bytes instead of %d bytes at byte %s from %s' %
                (len(byte_stream), blen, offset, fobj.name))
        return sha3_256(byte_stream).hexdigest()
    else:
        return None


def plain_fmt(name: str, h5obj, iter: bool = False, fobj: typing.Optional[typing.BinaryIO] = None):
    """Print storage information for each dataset in the file."""
    if isinstance(h5obj, h5py.Dataset):
        try:
            stinfo = storage_info(h5obj, use_iter=iter)
        except Exception as e:
            print('Caught exception for {}: {}'.format(h5obj.name, str(e)))
            return

        if len(stinfo) == 0:
            print('Dataset: {} has no data'.format(h5obj.name))
            return

        for index, si in enumerate(stinfo):
            cksum = get_cksum(fobj, si.byte_offset, si.size)
            if cksum is None:
                cksum_str = ''
            else:
                cksum_str = '; SHA-3-256: ' + cksum
            print('Dataset {}: index: {}; array offset: {}; '
                  'at byte {} of size {} bytes{}'
                  .format(h5obj.name, index, si.chunk_offset,
                          si.byte_offset, si.size, cksum_str))


def json_fmt(name, h5obj, iter=False, fobj=None, dict_=None):
    if isinstance(h5obj, h5py.Dataset):
        try:
            stinfo = storage_info(h5obj, use_iter=iter)
        except Exception as e:
            print('Caught exception for {}: {}'.format(h5obj.name, str(e)))
            return

        byte_streams = list()
        for index, si in enumerate(stinfo):
            byte_streams.append({'file_offset': si.byte_offset,
                                 'size': si.size,
                                 'index': index,
                                 'array_offset': si.chunk_offset,
                                 'uuid': str(uuid4())})
            cksum = get_cksum(fobj, si.byte_offset, si.size)
            if cksum:
                byte_streams[-1].update(
                    {'cksum': {'type': 'SHA-3-256', 'value': cksum}})
        dict_.update({h5obj.name: {'byteStreams': byte_streams}})

parser = argparse.ArgumentParser()
parser.add_argument('h5file', help='HDF5 file path or s3:// URI')
parser.add_argument('-j', help='Produce dataset storage info in JSON format',
                    action='store_true')
parser.add_argument('-c', help='Add SHA-3-256 checksum for each byte stream',
                    action='store_true')
parser.add_argument('-i', help='Use HDF5 chunk iterator feature (faster)',
                    action='store_true')
cli = parser.parse_args()

# Use anon mode if AWS access keys are not set
anon=False
for k in ('AWS_SECRET_ACCESS_KEY', 'AWS_ACCESS_KEY_ID'):
    if k not in environ:
        anon=True
        break
    v = environ[k]
    if not v:
        anon=True
        break
 
if cli.h5file.startswith('s3://'):
    s3 = s3fs.S3FileSystem(anon=anon, default_fill_cache=False)
    purl = urlparse(cli.h5file)
    h5s3 = s3.open(f'{purl.netloc}{purl.path}', mode='rb')
    h5f = h5py.File(h5s3, mode='r', driver='fileobj')
else:
    h5f = h5py.File(cli.h5file, 'r')

if cli.c:
    f = open(cli.h5file, 'rb')
    if not f.seekable():
        raise OSError('Byte stream for %s not seekable' % cli.h5file)
    f.seek(0, SEEK_SET)
else:
    f = None

if cli.j:
    stinfo = {cli.h5file: {}}
    h5f.visititems(partial(json_fmt, iter=cli.i, fobj=f, dict_=stinfo[cli.h5file]))
    print(json.dumps(stinfo))
else:
    h5f.visititems(partial(plain_fmt, iter=cli.i, fobj=f))
