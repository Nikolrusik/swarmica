FROM python:3.11-slim AS compile-image

ENV PYTHONUNBUFFERED=TRUE

RUN apt-get update \
    && apt-get install -y gcc libffi-dev libssl-dev\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --user --upgrade pip &&  pip3 install --user -r ./requirements.txt --no-cache-dir
RUN pip3 install --user gunicorn

FROM python:3.11-slim AS build-image

WORKDIR /swarmica

COPY --from=compile-image /root/.local /root/.local
COPY ./ /swarmica/

ENV PATH=/root/.local/bin:$PATH

RUN sleep 10