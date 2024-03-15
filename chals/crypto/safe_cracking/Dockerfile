FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat python3 python3-pip

RUN adduser chal

RUN mkdir -p /chal
WORKDIR /chal

COPY server.py ./
RUN chmod 555 server.py
USER chal

CMD socat -T60 TCP-LISTEN:1337,fork,reuseaddr EXEC:"python3 -u server.py",stderr
