# syntax=docker/dockerfile:experimental

FROM python:3.11-alpine3.19

COPY . /drf_auth
WORKDIR /drf_auth

RUN pip install -r requirements.txt 

EXPOSE 8000

RUN adduser --disabled-password book-user
USER book-user

CMD ["python", "config/manage.py", "runserver", "0.0.0.0:8000"]

