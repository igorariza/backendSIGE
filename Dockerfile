FROM python:3.7-alpine
MAINTAINER GroupAr Company

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt 
RUN pip3 install -r /requirements.txt 

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN pip3 install pipenv
RUN pipenv install 

RUN adduser -D myuser 
user myuser