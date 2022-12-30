# base docker image
FROM python:3.6-slim

# all the errors will be looged
ENV PYTHONUNBUFFERED 1

# sets your current working directory
WORKDIR /app

# copies current folder's files to docker image's app folder
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run the Django development server when the container launches
CMD ["python", "manage.py", "migrate"]