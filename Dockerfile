FROM alpine:latest

RUN apk  python3 && pip3 install --upgraded pip3

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirement.txt