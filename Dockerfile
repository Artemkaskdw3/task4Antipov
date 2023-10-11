FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip

COPY log.py /

CMD python3 log.py
