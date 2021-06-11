FROM continuumio/miniconda3:latest

LABEL MAINTAINER="Aleksandar Jelenak <help@hdfgroup.org>"
ARG HDF5_SRC_URL=http://www.hdfgroup.org/ftp/HDF5/releases
ARG HDF5_MAJOR_REL=1.10
ARG HDF5_MINOR_REL=6
ENV AWS_ACCESS_KEY_ID=SupplyCorrectValue
ENV AWS_SECRET_ACCESS_KEY=SupplyCorrectValue

# SHELL ["conda", "run", "-n", "base", "/bin/bash", "-c"]
RUN conda install -n base -y -c conda-forge \
        curl \
        python=3.9 \
        hdf5=${HDF5_MAJOR_REL}.${HDF5_MINOR_REL} \
        h5py=3.2.1 \
        s3fs=2021.5.0 \
    && \
    conda clean -a -y && \
    cd /usr/local/bin && \
    curl -O https://gist.githubusercontent.com/ajelenak/1babbf6e3a15a12cf0721ce8975017cf/raw/bb446ccdc63aeffa1a644075f55979590e6e9270/store_info.py

# Create a volume for external files...
RUN mkdir /data
VOLUME /data
WORKDIR /data

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "base", "python", "/usr/local/bin/store_info.py"]
CMD ["--help"]
