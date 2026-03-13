# Use a lightweight Python 3.9 base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install all Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose port 5000 so Flask app can be accessed from outside the container
EXPOSE 5000

# Run the Flask application when the container starts
CMD ["python", "app.py"]