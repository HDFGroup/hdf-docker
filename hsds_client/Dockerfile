FROM hdfgroup/python:3.7
LABEL MAINTAINER="John Readey, HDFGroup" 
ENV AWS_ACCESS_KEY_ID=SupplyCorrectValue
ENV AWS_SECRET_ACCESS_KEY=SupplyCorrectValue
ENV AWS_S3_GATEWAY==http://s3.amazonaws.com
ENV AWS_REGION=us-east-1
ENV HS_ENDPOINT=SupplyCorrectValue
ENV HS_USERNAME=SupplyCorreectValue
ENV HS_PASSWORD=SupplyCorrectValue

RUN apt-get -y install git \ 
&& conda install h5py \
&& pip install awscli \
&& pip --no-cache-dir install git+https://github.com/HDFGroup/h5pyd.git 
