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


## Starting the project using docker
- As I have dockerized the project you will have to **install docker on your system**

- Run the following commands to start the docker server
***docker compose up*** -> **builds all docker images mentioned in Dockerfile**

- Add v_host in rabbitmq server
***docker ps*** -> **returns all the docker images** copy the rabbitmq image id
***docker exec -it <rabbit_mq image id>***
***rabbitmqctl add_vhost guptaji*** -> **adds a virtual_host named guptaji**
***rabbitmqctl set_permissions -p guptaji guest ".*" ".*" ".*"*** -> **gives all permissions to guptaji**
***exit*** -> **exits the container**

- Run the following **commands to stop the container**
***docker ps*** -> **shows present state of all the containers**
***docker kill <container_id>*** -> **kills the given container**

- Once all the Containers are runnning

- Use this to Search based on title
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?title=Badi khabar'**

- Use this to Search based on description
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?description=Breaking News'**

- Use this to Search based on title and description
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?title=Badi khabar&description=Breaking News'**

- Use this to get videos
**curl --location --request GET 'http://localhost:8000/youtube/get_videos/?page=2&size=1'**

## Code is Extensible to add caching or other services like kafka.

