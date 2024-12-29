# Use Python as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY application.py .                 # Copy application.py to /app
COPY requirements.txt .               # Copy requirements.txt to /app
COPY Templates ./Templates            # Copy the entire Templates directory to /app/Templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Start the application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "application:application"]
