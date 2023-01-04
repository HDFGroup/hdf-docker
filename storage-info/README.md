# Docker Image for Retrieving HDF5 Dataset Storage Information

## Ingredients

* `continuumio/miniconda3@sha256:145567896379` Docker base image for the build stage
* conda 22.11.1
* `debian:bullseye-slim` as Docker base image for runtime
* Python 3.11
* HDF5 1.14.0
* Custom h5py from the d2709cee commit
* s3fs 2022.11.0
* A Python script to generate dataset storage maps for an input HDF5 file

## How to Use

Get the Docker image:

    docker pull hdfgroup/store_info.py

Detailed instructions:

```sh
docker run --rm hdfgroup/store_info.py
```

Produce HDF5 dataset storage map with chunk checksums in JSON:

```sh
docker run --rm -v DIR:/data hdfgroup/store_info.py -j -c /data/example.h5
```

`DIR` is the directory with the HDF5 file.

It is also possible to produce storage maps from HDF5 files in AWS S3:

```sh
docker run --rm \
           -e "AWS_ACCESS_KEY_ID=ABC" -e "AWS_SECRET_ACCESS_KEY=123" \
           hdfgroup/store_info.py s3://mybucket/myfile.h5
```

Use the `-i` option for a faster method to iterate over HDF5 dataset chunks:

```sh
docker run --rm -v DIR:/data hdfgroup/store_info.py -i /data/example.h5
```

## Example

For a file:

```
h5dump -Hp example.h5
HDF5 "example.h5" {
GROUP "/" {
   DATASET "DS1" {
      DATATYPE  H5T_STD_I32LE
      DATASPACE  SIMPLE { ( 6, 8 ) / ( 6, 8 ) }
      STORAGE_LAYOUT {
         CHUNKED ( 4, 4 )
         SIZE 256
      }
      FILTERS {
         NONE
      }
      FILLVALUE {
         FILL_TIME H5D_FILL_TIME_IFSET
         VALUE  H5D_FILL_VALUE_DEFAULT
      }
      ALLOCATION_TIME {
         H5D_ALLOC_TIME_INCR
      }
   }
}
}
```

the full JSON output including chunk checksums is:

```json
{
  "example.h5": {
    "/DS1": {
      "byteStreams": [
        {
          "file_offset": 4016,
          "size": 64,
          "index": 0,
          "array_offset": [
            0,
            0
          ],
          "uuid": "1b177f6c-5636-47e2-a963-560c85ecf939",
          "cksum": {
            "type": "SHA-3-256",
            "value": "295fcd26195b5817fdb96649cd80d2283be35ebc560fe2c727e874ced9af4474"
          }
        },
        {
          "file_offset": 4080,
          "size": 64,
          "index": 1,
          "array_offset": [
            0,
            4
          ],
          "uuid": "b4831613-3e2c-4991-aeb3-2a27c56e71f2",
          "cksum": {
            "type": "SHA-3-256",
            "value": "3113e65531696175672002c7a9955f809cd5f4580ee64cd154b39302d0442ed5"
          }
        },
        {
          "file_offset": 4144,
          "size": 64,
          "index": 2,
          "array_offset": [
            4,
            0
          ],
          "uuid": "3669a955-626b-4c17-9aff-47f0dd9b00ea",
          "cksum": {
            "type": "SHA-3-256",
            "value": "e0f12a55c640173301652c4016f573597ce8d431f7adbff02edc740880f07dc8"
          }
        },
        {
          "file_offset": 4208,
          "size": 64,
          "index": 3,
          "array_offset": [
            4,
            4
          ],
          "uuid": "5a61471e-0069-4efb-ab81-9ef123adf304",
          "cksum": {
            "type": "SHA-3-256",
            "value": "29eef5a0e2bbaebcc22e30f24f825bf149172d45f3c30e4108dba54b3a53a7ae"
          }
        }
      ]
    }
  }
}
```

## Advanced Features

The Python script supports several advanced features:

* `-i` option already mentioned. It uses the HDF5 chunk iterator.
  Always recommended.
* `--s3fslog=debug` will log each s3fs range request. This can show the number of S3 requests and where in the HDF5 file requested bytes are coming from.
* `--s3fs-block-size` to set new byte size of each s3fs range requests. Smaller range requests may sometimes yield better performance.
* `--s3fs-fill-cache` to turn on/off s3fs fill cache setting.
* `-pbs` HDF5 page buffering. Only applies for files created with paged aggregation. If set as greater or equal to the file's page size it can significantly improve performance.
