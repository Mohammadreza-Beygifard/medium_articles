# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application files and install dependencies in one step
COPY requirements.txt ./

# Combine the Python package installation and system package installation into a single RUN command
RUN apt-get update && apt-get install -y \
    curl \
    vim && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the source code after the install commands 
# to avoid reinstalling unnecessarily the dependencies in case of a code change
COPY app.py utils.py config.json ./

# Define environment variable
ENV APP_ENV=production

# Command to run the application
CMD ["python", "app.py"]