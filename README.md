# Flask App with Docker

This project demonstrates how to build and run a simple **Python Flask web application inside a Docker container**.

The goal of this project is to understand the fundamentals of:

* Containerization
* Docker images
* Docker containers
* Port mapping
* Docker image versioning
* Publishing images to Docker Hub

This is a **beginner-friendly Docker project** that helps developers learn how to package and run applications in containers.

---

# Project Overview

The application is a small Flask API with three endpoints:

| Endpoint  | Description                       |
| --------- | --------------------------------- |
| `/`       | Returns a welcome message         |
| `/health` | Health check endpoint             |
| `/info`   | Information about the application |

The Flask application runs inside a Docker container and can be accessed via a mapped host port.

---

# Project Structure

```
docker/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Application Code

## `app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This app is running inside a Docker container."

@app.route("/health")
def health_check():
    return "Healthy", 200

@app.route("/info")
def info():
    return "This is a Flask app running inside a Docker container."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

---

# Requirements

## `requirements.txt`

```
flask
```

---

# Docker Configuration

## Dockerfile

```dockerfile
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Flask application
CMD ["python", "app.py"]
```

---

# Build Docker Image

Build the Docker image using the following command:

```
docker build -t flask_image .
```

You can also build a **versioned Docker image**:

```
docker build -t junaidbilal005/custom_flask_image:0.0.1 .
```

This creates a tagged image that can later be pushed to Docker Hub.

---

# Run Docker Container

Run the container using:

```
docker run -d -p 5001:5000 --name flask_container flask_image
```

Explanation:

| Option                   | Description                               |
| ------------------------ | ----------------------------------------- |
| `-d`                     | Run container in background               |
| `-p 5001:5000`           | Maps host port 5001 → container port 5000 |
| `--name flask_container` | Container name                            |

---

# Access the Application

Open your browser:

```
http://127.0.0.1:5001
```

Available endpoints:

```
http://127.0.0.1:5001/
http://127.0.0.1:5001/health
http://127.0.0.1:5001/info
```

---

# Push Image to Docker Hub

Login to Docker Hub:

```
docker login
```

Push the image:

```
docker push junaidbilal005/custom_flask_image:0.0.1
```

This allows others to pull and run your image.

---

# Run Container from Docker Hub Image

```
docker run -d -p 5001:5000 junaidbilal005/custom_flask_image:0.0.1
```

---

# Useful Docker Commands

List running containers

```
docker ps
```

List all containers

```
docker ps -a
```

List images

```
docker images
```

Stop container

```
docker stop flask_container
```

Remove container

```
docker rm flask_container
```

Remove image

```
docker rmi flask_image
```

---

# Troubleshooting

## Port Already in Use

If you see an error like:

```
Bind for 0.0.0.0:5001 failed: port is already allocated
```

Check what is using the port:

```
lsof -i :5001
```

Or stop existing containers:

```
docker stop $(docker ps -aq)
```

---

# Technologies Used

* Python
* Flask
* Docker

---

# Learning Goals

This project demonstrates:

* Running applications in containers
* Creating Docker images
* Managing containers
* Port mapping
* Docker image versioning
* Publishing images to Docker Hub

---

# Author

**Junaid Bilal**
Senior Data Engineer

GitHub
https://github.com/junaidbilal5
