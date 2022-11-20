################# Builder ###############
FROM python:3.7-alpine as base

COPY ./requirements.txt .


RUN \
    apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev openssl-dev libffi-dev g++ build-base linux-headers postgresql-dev postgresql-contrib pcre-dev bash alpine-sdk libpq libjpeg-turbo libstdc++ && \
    pip install wheel && \
    pip install -r requirements.txt && \
    apk del .build-deps


RUN pip install -r requirements.txt

################# Release ###############
FROM python:3.7-alpine AS release

RUN apk add --update --no-cache bash libpq

COPY --from=base /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV PATH=/root/local/bin:$PATH

WORKDIR /src
RUN mkdir /src/staticfiles

COPY . /src/

