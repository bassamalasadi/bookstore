FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /bookstore
WORKDIR /bookstore

COPY requirements.txt /bookstore/requirements.txt
RUN pip install -r requirements.txt
ADD . /bookstore/
