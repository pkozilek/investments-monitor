FROM ubuntu:18.04
LABEL 'maintainer' = 'mindminers'

ARG DASH_HOME=/usr/local/dash

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip install  --upgrade pip \
  && pip3 install numpy==1.19.5  \
  && pip3 install pandas==1.1.5 \
  && pip3 install dash==1.20.0 \
  && pip3 install requests==2.25.1 \
  && pip3 install dash-bootstrap-components==0.12.2

RUN pip install openpyxl

EXPOSE 8050

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR ${DASH_HOME}
