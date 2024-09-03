FROM python:3.10
LABEL maintainer="John Readey <jreadey@hdfgroup.org>"
ENV HDF5_MINOR_REL_URL      hdf5_1.14.4.3
ENV HDF5_MINOR_REL_FOLDER   hdf5-1.14.4-3
ENV HDF5_SRC_URL         https://github.com/HDFGroup/hdf5/releases/download

# Install the necessary packages
RUN cd /tmp && \
    apt-get --yes update && \
    apt-get --yes install cmake

# Download the HDF5 source code
RUN wget -q ${HDF5_SRC_URL}/${HDF5_MINOR_REL_URL}/hdf5.tar.gz && \
    tar -xzf hdf5.tar.gz --directory /usr/local/src && \
    rm hdf5.tar.gz

# Configure the library
RUN cd /usr/local/src/${HDF5_MINOR_REL_FOLDER} && \
    mkdir build && \
    cd build && \
    cmake -DHDF5_ENABLE_ROS3_VFD=ON -DCMAKE_INSTALL_PREFIX=/usr/local/hdf5 -S .. -B .

# Build and install the library
RUN cd /usr/local/src/${HDF5_MINOR_REL_FOLDER}/build && \
    cmake --build . --config Release -j

RUN cd /usr/local/src/${HDF5_MINOR_REL_FOLDER}/build && \
    cmake --install .

# Clean up
RUN rm -rf /usr/local/src/${HDF5_MINOR_REL_FOLDER}/* 

# Set up executables
RUN for f in /usr/local/hdf5/bin/* ; do ln -s $f /usr/local/bin ; done

# Install the necessary Python packages
RUN pip install cython && \
    pip install numpy && \
    pip install s3fs

# Install h5py
RUN cd /usr/local/src && \
    git clone https://github.com/h5py/h5py.git && \
    cd h5py && \
    export HDF5_DIR=/usr/local/hdf5 && \
    pip install -v .

# Install h5pyd
RUN cd /usr/local/src && \
    git clone https://github.com/HDFGroup/h5pyd.git && \
    cd h5pyd && \
    pip install -v .                                                             
