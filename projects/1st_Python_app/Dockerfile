#pull base image for python, slim image are light weight
FROM python:3.9-slim
# set the working directory in the container
WORKDIR /app
# copy the current directory contents into the container at /app
COPY . /app
# install any needed packages specified in requirements.txt
##RUN pip install --no-cache-dir -r requirements.txt
# make port 80 available to the world outside this container
##EXPOSE 80
# define environment variable
##ENV NAME World
# run app.py when the container launches
CMD ["python", "app.py"]

#we basically create the app folder in the image

