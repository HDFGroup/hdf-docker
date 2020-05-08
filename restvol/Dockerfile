FROM centos
MAINTAINER John Readey <jreadey@hdfgroup.org>                                                           
RUN yum -y install gcc gcc-c++                                                        ; \
    yum -y install yajl                                                               ; \
    yum -y install wget                                                               ; \
    yum -y install unzip                                                              ; \
    yum -y install make                                                               ; \
    yum -y install which                                                              ; \
    yum -y install autofconf                                                          ; \
    yum -y install libtool                                                            ; \
    yum -y install curl-devel                                                         ; \
    yum -y install openssl-devel                                                      ; \
    yum -y install git                                                                
RUN cd /tmp                                                                           ; \
    wget https://github.com/Kitware/CMake/releases/download/v3.17.2/cmake-3.17.2.tar.gz ;\
    gunzip cmake-3.17.2.tar.gz                                                        ; \
    tar -xvf cmake-3.17.2.tar                                                         ; \
    cd cmake-3.17.2                                                                   ; \
    ./bootstrap                                                                       ; \
    make                                                                              ; \
    make install                                                                      
RUN cd /usr/local/src                                                                 ; \
    git clone  https://github.com/lloyd/yajl                                          ; \
    cd yajl                                                                           ; \
    mkdir build                                                                       ; \
    cd build                                                                          ; \
    cmake ..                                                                          ; \
    make                                                                              ; \
    cp -R yajl-2.1.1/include/yajl /usr/local/include                                  ; \
    cp yajl-2.1.1/lib/* /usr/local/lib                                                ; \
    cd /usr/local
RUN cd /usr/local/src                                                                 ; \
    git clone https://bitbucket.hdfgroup.org/scm/hdf5vol/rest.git -b  hdf5_1_12_update    ; \
    cd rest                                                                           ; \
    ./build_vol_cmake.sh -P /usr/local/



 