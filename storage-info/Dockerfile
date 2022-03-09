FROM continuumio/miniconda3@sha256:92d7896124d940cb1815d3b59d8eaab9a8e86c801af2437658581465044b0a06 AS app-base

LABEL maintainer="Aleksandar Jelenak <help@hdfgroup.org>"

RUN conda config --add channels conda-forge && \
    conda config --set channel_priority strict && \
    conda install conda-pack --yes && \
    conda create --name app --yes python=3.9
RUN conda install --name app --yes \
        curl \
        git \
        tar \
        gzip \
        c-compiler \
        make \
        cmake \
        pkg-config \
        pip \
        numpy \
        cython \
        pkgconfig \
        s3fs=2021.11.1
SHELL ["conda", "run", "-n", "app", "--no-capture-output", "/bin/sh", "-c"]
WORKDIR /scratch
RUN curl -O https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.13/hdf5-1.13.0/src/hdf5-1.13.0.tar.gz && \
    tar xzvf hdf5-1.13.0.tar.gz
RUN mkdir build && \
    cd build && \
    cmake . \
          -S ../hdf5-1.13.0 \
          -G "Unix Makefiles" \
          -DCMAKE_INSTALL_PREFIX=${CONDA_PREFIX} \
          -DCMAKE_BUILD_TYPE=Release \
          -DHDF5_ENABLE_SYMBOLS=OFF \
          -DBUILD_SHARED_LIBS=ON \
          -DHDF5_ENABLE_ALL_WARNINGS=OFF \
          -DHDF5_ENABLE_THREADSAFE=OFF \
          -DHDF5_BUILD_HL_LIB=ON \
          -DHDF5_ENABLE_PARALLEL=OFF \
          -DHDF5_BUILD_CPP_LIB=OFF \
          -DHDF5_BUILD_FORTRAN=OFF \
          -DHDF5_BUILD_JAVA=OFF \
          -DHDF5_BUILD_TOOLS=OFF \
          -DHDF5_ENABLE_ROS3_VFD=OFF \
          -DHDF5_ENABLE_Z_LIB_SUPPORT=OFF \
          -DHDF5_ENABLE_SZIP_SUPPORT=OFF \
          -DBUILD_TESTING=OFF \
          ${CMAKE_ARGS} \
    && \
    cmake --build . --config Release && \
    cmake --install ./ -v
RUN H5PY_SETUP_REQUIRES=0 HDF5_DIR=${CONDA_PREFIX} \
    pip install git+https://github.com/ajelenak/h5py.git@073d8e24f5f3079e76b0a97f4e16e9f498617202 --no-deps --no-build-isolation
SHELL ["/bin/sh", "-c"]
RUN conda remove -n app --yes \
        git \
        tar \
        gzip \
        c-compiler \
        make \
        cmake
RUN conda-pack -n app -o env.tar && \
    mkdir -p /opt/env/app && \
    tar xf env.tar -C /opt/env/app && \
    /opt/env/app/bin/conda-unpack

#
#
#

FROM debian:bullseye-slim

LABEL maintainer="Aleksandar Jelenak <help@hdfgroup.org>"

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

COPY --from=app-base /opt/env/app /opt/env/app

COPY store_info.py /opt/env/app/bin/
 
# Create a volume for external files...
RUN mkdir /data
VOLUME /data
WORKDIR /data

ENTRYPOINT ["/opt/env/app/bin/python", "/opt/env/app/bin/store_info.py"]
CMD ["--help"]
