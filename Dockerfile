FROM python:3

# vimとseleniumをインストール
RUN set -x && \
    apt-get update && \
    apt-get install -y vim && \
    pip install selenium

RUN mkdir -p /root/workdir

COPY ./app /root/workdir
WORKDIR /root/workdir
