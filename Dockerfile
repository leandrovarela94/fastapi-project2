FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./poetry.lock /
COPY ./pyproject.toml /

RUN apt-get update && \
    apt-get install -y sudo curl python3 && \
    curl -sSL https://install.python-poetry.org | python3 -


COPY . .
WORKDIR /app

RUN poetry config virtualenvs.create false 
RUN poetry install 