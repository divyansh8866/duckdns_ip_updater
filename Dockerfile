# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org requests

# Define environment variable
ENV DUCKDNS_TOKEN=xxx
ENV DUCKDNS_DOMAIN=xxx

# Run script when the container launches
CMD ["python", "script.py"]
