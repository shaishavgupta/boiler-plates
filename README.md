# FamPay-YouTube-Assignment

## Clone the repo

## Starting the project
- As I have dockerized the project you will have to **install docker on your system**

- Run the following commands to start the docker server
***docker build . -t fampay_youtube_django*** -> **builds docker images and follows above steps**
***docker run -d -p 8000:8000 fampay_youtube_django*** -> **runs docker container in detatched mode**

- Run the following **commands to stop the container**
***docker ps*** -> **shows present state of all the containers**
***docker kill <container_id>*** -> **kills the given container**

- Once the Container is runnning

- Use this to Search based on title
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?title=Badi khabar'**

- Use this to Search based on description
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?description=Breaking News'**

- Use this to Search based on title and description
**curl --location --request GET 'http://127.0.0.1:8000/youtube/search/?title=Badi khabar&description=Breaking News'**

- Use this to get videos 
**curl --location --request GET 'http://localhost:8000/youtube/get_videos/?page=2&size=1'**