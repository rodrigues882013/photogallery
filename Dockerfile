FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/application
COPY . /usr/src/application

WORKDIR /usr/src/application

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

WORKDIR /usr/src/application/photogallery
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]

# Django service
EXPOSE 8000