# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application runs on
EXPOSE 5000  

# Command to run the application
CMD ["python", "app/__init__.py"]
