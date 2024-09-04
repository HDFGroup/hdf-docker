FROM dokken/centos-stream-9
LABEL maintainer="John Readey <jreadey@hdfgroup.org>"
                                                       
RUN yum -y install gcc gcc-c++                                                        ; \
    yum -y install wget                                                               ; \
    yum -y install unzip                                                              ; \
    yum -y install make                                                               ; \
    yum -y install which                                                              ; \
    yum -y install libtool                                                            ; \
    yum -y install curl-devel                                                         ; \
    yum -y install openssl-devel                                                      ; \
    yum -y install git                                                                
RUN cd /tmp                                                                           ; \
    wget https://github.com/Kitware/CMake/releases/download/v3.29.1/cmake-3.29.1.tar.gz ;\
    gunzip cmake-3.29.1.tar.gz                                                        ; \
    tar -xvf cmake-3.29.1.tar                                                         ; \
    cd cmake-3.29.1                                                                   ; \
    ./bootstrap                                                                       ; \
    make                                                                              ; \
    make install                                                                      
RUN cd /usr/local/src                                                                 ; \
    git clone  https://github.com/lloyd/yajl                                          ; \
    cd yajl                                                                           ; \
    mkdir build                                                                       ; \
    cd build                                                                          ; \
    cmake -DCMAKE_INSTALL_PREFIX=/usr ..                                              ; \
    make                                                                              ; \
    make install                                                                      ; \
    cp -R yajl-2.1.1/include/yajl /usr/local/include                                  ; \
    cp yajl-2.1.1/lib/* /usr/local/lib                                                ; \
    cd /usr/local
RUN cd /usr/local/src                                                                 ; \
    git clone https://github.com/HDFGroup/hdf5                                        ; \
    cd hdf5                                                                           ; \
    mkdir build                                                                       ; \
    cd build                                                                          ; \
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/ -DCMAKE_BUILD_TYPE=Release -DBUILD_STATIC_LIBS=OFF -DHDF5_ENABLE_Z_LIB_SUPPORT=OFF -DHDF5_ENABLE_SZIP_SUPPORT=OFF .. ; \
    cmake --build . -j                                                                 ; \
    cmake --install .
RUN cd /usr/local/src                                                                 ; \
    git clone  https://github.com/HDFGroup/vol-rest                                   ; \
    cd vol-rest                                                                       ; \
    ./build_vol_cmake.sh -P /usr/local/



 