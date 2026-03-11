# Flask App with Docker

This project demonstrates how to build and run a simple **Python Flask web application inside a Docker container**.  
It is a basic example to understand **containerization, Docker images, and port mapping**.

---

## Project Overview

The application is a small Flask API with three endpoints:

- `/` → Returns a welcome message  
- `/health` → Health check endpoint  
- `/info` → Information about the application  

The app runs inside a Docker container and can be accessed through a mapped host port.

---

## Project Structure

```
docker/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Application Code

### `app.py`

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

## Requirements

### `requirements.txt`

```
flask
```

---

## Docker Configuration

### `Dockerfile`

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

## Build Docker Image

Run the following command inside the project directory:

```bash
docker build -t flask_image .
```

---

## Run Docker Container

```bash
docker run -p 5001:5000 --name flask_container flask_image
```

Explanation:

- `5001` → Host machine port  
- `5000` → Port used by Flask inside the container

---

## Access the Application

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

## Useful Docker Commands

List containers

```bash
docker ps
```

List all containers

```bash
docker ps -a
```

Stop container

```bash
docker stop flask_container
```

Remove container

```bash
docker rm flask_container
```

Remove image

```bash
docker rmi flask_image
```

---

## Technologies Used

- Python
- Flask
- Docker

---

## Author

**Junaid Bilal**  
Senior Data Engineer  

GitHub:  
https://github.com/junaidbilal5