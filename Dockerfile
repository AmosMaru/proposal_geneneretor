# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5553 to the outside world
EXPOSE 5553

# Load environment variables from .env file
CMD ["python", "-m", "dotenv", "-f", ".env", "python", "app.py"]
