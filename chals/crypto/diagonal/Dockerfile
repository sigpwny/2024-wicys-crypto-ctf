FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat python3

RUN adduser chal

RUN mkdir -p /chal
WORKDIR /chal

COPY chal.py flag.txt ./
RUN chmod 555 chal.py
USER chal

CMD socat -T60 TCP-LISTEN:1337,fork,reuseaddr EXEC:"python3 -u chal.py",stderr
