# base docker image
FROM python:3.6-slim

# all the errors will be looged
ENV PYTHONUNBUFFERED 1


# sets your current working directory
WORKDIR /fampay_youtube_assignment

# copies current folder's files to docker image's fampay_youtube_assignment folder
COPY . ./
RUN pip install -r requirements.txt

# publically exposes the 8000 port of the container
EXPOSE 8000

ENTRYPOINT rabbitmq-server && celery -A main worker -l info && celery -A main beat -l info

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0:8000