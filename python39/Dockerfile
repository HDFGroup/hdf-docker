FROM python:3.9

COPY entrypoint.sh /

# install system packages
RUN apt-get -y update              ; \
    apt-get -y install curl        ; \
    apt-get -y install wget        ; \
    apt-get -y install git         ; \
    apt-get -y install vim         ; \
    apt-get -y install hdf5-tools

#  pip install packages
RUN pip install numpy,             ; \
    install pytz                   ; \
    pip install awscli             ; \
    pip install numcodecs          ; \
    pip install h5py               ; \ 
    pip install pandas             ; \
    pip install h5netcdf           ; \
    pip install xarray             ; \
    pip install git+https://git@github.com/HDFGroup/h5pyd  


# setup home directory for h5user
RUN adduser h5user                ; \
    mkdir /home/h5user            ; \
    chown h5user /home/h5user    ; \
    echo "export PS1='\u@\h:\w $ '" >> /home/h5user/.bashrc ; \
    chown h5user /home/h5user/.bashrc

USER h5user

WORKDIR /home/h5user

# entrypoint will just sleep forever to keep the 
# container alive
ENTRYPOINT ["/bin/bash", "-c", "/entrypoint.sh"]
