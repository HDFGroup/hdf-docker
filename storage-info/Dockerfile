FROM python:3.8-alpine
LABEL MAINTAINER="Aleksandar Jelenak, The HDF Group"
ARG HDF5_SRC_URL=http://www.hdfgroup.org/ftp/HDF5/releases
ARG HDF5_MAJOR_REL=hdf5-1.10
ARG HDF5_MINOR_REL=6
ENV AWS_ACCESS_KEY_ID=SupplyCorrectValue
ENV AWS_SECRET_ACCESS_KEY=SupplyCorrectValue
RUN apk add --no-cache --virtual .build-deps \
        coreutils \
        gcc \
        g++ \
        libc-dev \
        make \
        zlib-dev \
        curl \
        git \
# Build and install HDF5 library...
 && cd /tmp \
 && curl -L -O ${HDF5_SRC_URL}/${HDF5_MAJOR_REL}/${HDF5_MAJOR_REL}.${HDF5_MINOR_REL}/src/${HDF5_MAJOR_REL}.${HDF5_MINOR_REL}.tar.gz \
 && tar -xzvf ${HDF5_MAJOR_REL}.${HDF5_MINOR_REL}.tar.gz \
 && cd ${HDF5_MAJOR_REL}.${HDF5_MINOR_REL} \
 && ./configure --prefix=/usr/local \
 && make -j "$(nproc)" \
 && make install \
 && cd .. \
 && rm -rf ${HDF5_MAJOR_REL}.${HDF5_MINOR_REL}* \
# Install h5py Python dependencies...
 && pip --no-cache-dir install -U pip \
 && pip --no-cache-dir install numpy Cython six pkgconfig s3fs \
# Install h5py from source...
 && pip --no-cache-dir install git+https://github.com/h5py/h5py.git@c69fc627c96aafcc1393bb70115e5bcd3a6f8a95 \
 && cd /usr/local/bin \
 && curl -O https://gist.githubusercontent.com/ajelenak/1babbf6e3a15a12cf0721ce8975017cf/raw/bb446ccdc63aeffa1a644075f55979590e6e9270/store_info.py \
 && apk del .build-deps

# Create a volume for external files...
RUN mkdir /data
VOLUME /data
WORKDIR /data

ENTRYPOINT ["python", "/usr/local/bin/store_info.py"]
CMD ["--help"]
