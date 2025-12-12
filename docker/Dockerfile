# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies (if you have requirements.txt)
# RUN pip install -r requirements.txt

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Default command
ENTRYPOINT ["./entrypoint.sh"]
