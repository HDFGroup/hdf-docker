FROM conda/miniconda3

# curl is needed to get credentials when using IAM_ROLE
RUN apt-get -y update              ; \
    apt-get -y install curl

    
# conda  install package
RUN conda install -y numpy                   ; \
    conda install -y aiobotocore=0.10.0      ; \
    conda install -y pytz                    ; \
    conda install -y requests                ; \
    conda install psutil                     ; \
    conda install numba           
