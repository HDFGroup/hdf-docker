FROM conda/miniconda3

RUN conda update -n base -c defaults conda -y

# curl is needed to get credentials when using IAM_ROLE
RUN apt-get -y update              ; \
    apt-get -y install curl

# conda  install package
RUN conda install -y numpy                   ; \
    conda install -y aiobotocore             ; \
    conda install -y pytz                    ; \
    conda install -y requests                ; \
    conda install -y psutil                  ; \
    conda install -y  numba                  ; \
    pip install kubernetes
