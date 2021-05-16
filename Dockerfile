FROM python:3-alpine

WORKDIR /bookgame
RUN apk update
RUN python3 -m pip install -U pip
RUN python3 -m pip install justpy markovify 
ADD . /bookgame 
ENTRYPOINT python3 bookgame.py
