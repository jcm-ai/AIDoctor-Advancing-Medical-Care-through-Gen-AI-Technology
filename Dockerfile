# Use Python 3.8 slim base image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY . /app

# Install system dependencies and Python packages
RUN pip install  -r requirements.txt

# Command to run the application
CMD ["python3", "app.py"]