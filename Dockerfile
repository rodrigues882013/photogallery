FROM python:3-alpine

RUN mkdir -p /usr/src/application
WORKDIR /usr/src/application

COPY . /usr/src/application
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["manage.py", "runserver" ]

# Expose the Django port
EXPOSE 8000