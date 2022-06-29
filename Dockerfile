FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /code

WORKDIR /code

COPY /backend /code/

COPY /requirements.txt /code/

RUN pip install -r requirements.txt
