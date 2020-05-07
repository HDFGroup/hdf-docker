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
    yum -y install cmake                                                              ; \
    yum -y install git                                                                ; \
    ln -s /usr/bin/cmake /usr/local/bin                                               ; \
    cd /usr/local/src                                                                 ; \
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
    git clone https://bitbucket.hdfgroup.org/scm/hdf5vol/rest.git                     ; \
    cd rest                                                                           ; \
    git checkout hddf5_1_12_update                                                    ; \
    ./build_vol_cmake.sh -P /usr/local/



 