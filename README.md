# FamPay-YouTube-Assignment

## Clone the repo

## Starting the project
- **install Rabbitmq**

- start rabbitmq server using **rabbitmq-server start**

- start celery beat server using **celery -A main beat -l INFO**

- start celery worker server using **celery -A main worker -l INFO**

- start the application using **python manage.py runserver**

- Use this to Search based on title
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?title=Badi khabar'**

- Use this to Search based on description
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?description=Breaking News'**

- Use this to Search based on title and description
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?title=Badi khabar&description=Breaking News'**

- Use this to get videos
**curl --location --request GET 'http://localhost:8000/youtube/get_videos/?page=2&size=1'**


## Code is Extensible to add caching or other services like kafka.