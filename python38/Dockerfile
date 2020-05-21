FROM conda/miniconda3

RUN conda update -n base -c defaults conda -y

# curl is needed to get credentials when using IAM_ROLE
RUN apt-get -y update              ; \
    apt-get -y install curl

# need to use conda for psutil
RUN conda install -y psutil

#  pip install packages
RUN pip install numpy                  ; \
    pip install pytz                   ; \
    pip install requests               ; \
    pip install numba                  ; \
    pip install 'aiobotocore<1'        ; \
    pip install kubernetes             ; \
    pip install azure-storage-blob     ; \
    pip install aiofiles               ; \
    pip install aiohttp		       ; \
    pip install aiohttp-cors           ; \
    pip install pyjwt                  ; \
    pip install pyyaml
