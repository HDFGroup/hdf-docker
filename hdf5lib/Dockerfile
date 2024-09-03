FROM python:3.10
MAINTAINER John Readey <jreadey@hdfgroup.org>
ENV HDF5_MAJOR_REL       hdf5-1.14
ENV HDF5_MINOR_REL       hdf5-1.14.3
ENV HDF5_SRC_URL   http://support.hdfgroup.org/ftp/HDF5/releases
RUN cd /tmp                                                                        ; \
    apt-get --yes update ;\
    apt-get --yes install cmake ;\
    echo "Getting: ${HDF5_SRC_URL}/${HDF5_MAJOR_REL}/${HDF5_MINOR_REL}/src/${HDF5_MINOR_REL}.tar"                ; \
    wget -q ${HDF5_SRC_URL}/${HDF5_MAJOR_REL}/${HDF5_MINOR_REL}/src/${HDF5_MINOR_REL}.tar                        ; \
    tar -xf ${HDF5_MINOR_REL}.tar --directory /usr/local/src                      ; \
    rm ${HDF5_MINOR_REL}.tar                                                       ; \
    cd /usr/local/src/${HDF5_MINOR_REL}                                            ; \
    ./configure --prefix=/usr/local/hdf5                                           ; \
    mkdir build                                                                    ; \
    cd build                                                                       ; \
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/hdf5                                   ; \
    cmake --build . -j                                                             ; \
    cmake --install .                                                              ; \
    sleep 5 ; \
    rm -rf /usr/local/src/${HDF5_MINOR_REL}/*                                      ; \
    for f in /usr/local/hdf5/bin/* ; do ln -s $f /usr/local/bin ; done             ; \
    pip install cython                                                             ; \
    pip install numpy                                                              ; \
    pip install s3fs                                                               ; \
    cd /usr/local/src                                                              ; \
    git clone https://github.com/h5py/h5py.git                                     ; \
    cd h5py                                                                        ; \
    export HDF5_DIR=/usr/local/hdf5                                                ; \
    pip install -v .                                                               ; \
    cd -                                                                           ; \
    git clone https://github.com/HDFGroup/h5pyd.git                                ; \
    cd h5pyd                                                                       ; \
    pip install -v . ; \
    cd -                                                                           
