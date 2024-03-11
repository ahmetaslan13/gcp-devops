# Use Python 3.8 slim buster as base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Specify the default command to run when the container starts
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
