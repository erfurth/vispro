# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies (requirements.txt)
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project files
COPY . /app

# Expose the ports
EXPOSE 5000 8050

# Command to run the application
CMD ["python", "app.py"]
