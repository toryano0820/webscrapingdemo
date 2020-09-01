FROM python:3.6-slim

RUN apt update \
    && apt install build-essential -y \
    && apt clean

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt
