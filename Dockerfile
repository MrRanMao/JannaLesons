# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash docker
USER docker
WORKDIR /core

COPY ./requirements.txt /core/requirements.txt
RUN pip install --upgrade pip && pip install -r /core/requirements.txt --upgrade
COPY . /core/