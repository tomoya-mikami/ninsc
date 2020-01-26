FROM python:3.7-alpine

# Headless Chrome準備
RUN apk update
RUN apk add ttf-freefont chromium chromium-chromedriver
RUN pip install selenium

# 日本語対応
RUN mkdir /font
ADD https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip /font
WORKDIR /font
RUN unzip NotoSansCJKjp-hinted.zip && \
    mkdir -p /usr/share/fonts/noto && \
    cp *.otf /usr/share/fonts/noto && \
    chmod 644 -R /usr/share/fonts/noto/ && \
    fc-cache -fv
RUN rm -rf /font

# ディレクトリ準備
RUN mkdir -p /root/workdir
COPY ./app /root/workdir
WORKDIR /root/workdir
