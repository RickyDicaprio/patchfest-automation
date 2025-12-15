# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Make entrypoint executable
RUN chmod +x docker/entrypoint.sh

# Default command
ENTRYPOINT ["./docker/entrypoint.sh"]
