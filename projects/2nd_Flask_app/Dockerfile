FROM python:3.8-slim

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app
#COPY . .


#add the requirements.txt
#COPY requirements.txt /app/requirements.txt


# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# run app.py when the container launches
CMD ["python", "app.py"]

#we basically create the app folder in the image

