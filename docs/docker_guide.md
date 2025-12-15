# Docker Guide

## What is Docker?

Docker is a platform that allows you to package applications and their dependencies into lightweight, portable containers. Think of containers as mini virtual machines that contain everything needed to run your application - code, runtime, system libraries, and settings.

**Key Benefits:**
- **Consistency**: Your application runs the same way everywhere (development, testing, production)
- **Isolation**: Applications don't interfere with each other
- **Portability**: Works on any system that supports Docker
- **Efficiency**: Lighter than traditional virtual machines

**Docker vs Traditional Setup:**
- Without Docker: You need to install Python, dependencies, and configure your system
- With Docker: Everything is pre-configured in a container - just run one command!

## Installation

### Windows
1. Download Docker Desktop from https://docs.docker.com/desktop/install/windows-install/
2. Run the installer and follow setup wizard
3. Restart your computer when prompted
4. Open Docker Desktop and complete the initial setup
5. Verify installation:
   ```cmd
   docker --version
   docker compose --version
   ```

### macOS
1. Download Docker Desktop from https://docs.docker.com/desktop/install/mac-install/
2. Drag Docker.app to Applications folder
3. Launch Docker Desktop from Applications
4. Grant necessary permissions when prompted
5. Verify installation:
   ```bash
   docker --version
   docker compose --version
   ```

### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt update

# Install dependencies
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to docker group (to avoid using sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker compose --version
```

## Project Docker Structure

Our project uses Docker to provide a consistent development environment. Here's how it's organized:

```
docker/
├── Dockerfile              # Main container definition
├── docker-compose.yml      # Multi-container orchestration
└── entrypoint.sh           # Container startup script
```

### Dockerfile Explained

```dockerfile
# Base image - Python 3.10 on minimal Linux
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files to container
COPY . /app

# Install Python dependencies
# RUN pip install -r requirements.txt

# Make startup script executable
RUN chmod +x entrypoint.sh

# Run startup script when container starts
ENTRYPOINT ["./entrypoint.sh"]
```

**Each line explained:**
- `FROM python:3.10-slim`: Use official Python image as base
- `WORKDIR /app`: Set `/app` as working directory
- `COPY . /app`: Copy project files from host to container
- `RUN chmod +x entrypoint.sh`: Make script executable
- `ENTRYPOINT ["./entrypoint.sh"]`: Run script when container starts

## Docker Commands

### Building the Image
```bash
# Build image with a name tag
docker build -t patchfest-automation .

# Build from specific directory
docker build -t patchfest-automation -f docker/Dockerfile .

# Build with no cache (fresh build)
docker build --no-cache -t patchfest-automation .
```

### Running Containers
```bash
# Basic run (container stops when command finishes)
docker run patchfest-automation

# Run with interactive terminal
docker run -it patchfest-automation /bin/bash

# Run in background (detached mode)
docker run -d --name my-automation patchfest-automation

# Run with port mapping (if your app serves on a port)
docker run -p 8080:8080 patchfest-automation

# Run with volume mount (share files with host)
docker run -v $(pwd)/scripts:/app/scripts patchfest-automation
```

### Container Management
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a running container
docker stop container-name-or-id

# Start a stopped container
docker start container-name-or-id

# Remove a container
docker rm container-name-or-id

# Remove all stopped containers
docker container prune
```

### Interactive Container Access
```bash
# Execute bash in running container
docker exec -it container-name /bin/bash

# Execute a single command
docker exec container-name python scripts/sample_hello.py

# Execute with specific user
docker exec -u root -it container-name /bin/bash
```

### Image Management
```bash
# List all images
docker images

# Remove an image
docker rmi image-name-or-id

# Remove unused images
docker image prune
```

## Docker Compose Workflow

Docker Compose simplifies multi-container applications:

```bash
# Build and start all services
docker compose up --build

# Start services in background
docker compose up -d

# View logs
docker compose logs

# Stop all services
docker compose down

# Stop and remove volumes
docker compose down -v
```

## Example Workflow: Running This Project

### Method 1: Using Docker Compose (Recommended)
```bash
# 1. Clone the repository
git clone <repository-url>
cd patchfest-automation

# 2. Build and run with Docker Compose
docker compose up --build

# 3. Run specific scripts
docker compose run automation_scripts python scripts/sample_hello.py
docker compose run automation_scripts python scripts/backup_folder.py --help

# 4. Clean up when done
docker compose down
```

### Method 2: Using Docker Commands
```bash
# 1. Build the image
docker build -t patchfest-automation .

# 2. Run scripts
docker run patchfest-automation python scripts/sample_hello.py
docker run -v $(pwd)/data:/app/data patchfest-automation python scripts/backup_folder.py /app/data /app/backup

# 3. Interactive development
docker run -it -v $(pwd):/app patchfest-automation /bin/bash
```

## Docker Workflow Diagram

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Dockerfile    │    │  Docker Image   │    │ Docker Container│
│                 │    │                 │    │                 │
│ Instructions    │───▶│  Built Image    │───▶│  Running App    │
│ Dependencies    │    │  (Snapshot)     │    │  (Live Process) │
│ Configuration   │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                        │                        │
        │ docker build           │ docker run             │ docker exec
        ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Build Process   │    │ Container Start │    │ Execute Commands│
│                 │    │                 │    │                 │
│ • Download base │    │ • Create runtime│    │ • Run scripts   │
│ • Install deps  │    │ • Mount volumes │    │ • Debug issues  │
│ • Copy files    │    │ • Start services│    │ • View logs     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Common Errors & Fixes

### "Docker command not found"
**Problem:** Docker is not installed or not in PATH
**Solution:**
- Install Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Restart terminal after installation
- Verify with `docker --version`

### "Permission denied" (Linux)
**Problem:** User not in docker group
**Solution:**
```bash
sudo usermod -aG docker $USER
newgrp docker
# or logout and login again
```

### "Port already in use"
**Problem:** Another process is using the port
**Solution:**
```bash
# Find what's using the port
lsof -i :8080

# Use a different port
docker run -p 8081:8080 your-app

# Kill the process using the port
sudo kill -9 <PID>
```

### "No space left on device"
**Problem:** Docker has consumed all disk space
**Solution:**
```bash
# Clean up unused containers, images, and volumes
docker system prune -a

# Remove specific containers/images
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
```

### "Container exits immediately"
**Problem:** Container command finishes or fails
**Solution:**
```bash
# Run with interactive mode to see what happens
docker run -it your-image /bin/bash

# Check logs
docker logs container-name

# Override entrypoint for debugging
docker run -it --entrypoint=/bin/bash your-image
```

### "Could not connect to Docker daemon"
**Problem:** Docker service is not running
**Solution:**
```bash
# Start Docker Desktop (Windows/Mac)
# Or start Docker service (Linux)
sudo systemctl start docker
```

## Best Practices

### 1. Use .dockerignore
Create a `.dockerignore` file to exclude unnecessary files:
```
.git
.gitignore
node_modules
*.log
.DS_Store
Thumbs.db
```

### 2. Keep Images Small
- Use slim base images (`python:3.10-slim` vs `python:3.10`)
- Remove package managers after installation
- Use multi-stage builds for complex applications

### 3. Don't Run as Root
```dockerfile
# Create non-root user
RUN useradd -m appuser
USER appuser
```

### 4. Use Specific Tags
```dockerfile
# Good: specific version
FROM python:3.10-slim

# Bad: latest can change
FROM python:latest
```

### 5. Layer Caching
```dockerfile
# Copy requirements first (better caching)
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

## Troubleshooting Tips

1. **Always check logs:** `docker logs container-name`
2. **Use interactive mode:** `docker run -it` for debugging
3. **Check container status:** `docker ps -a`
4. **Clean up regularly:** `docker system prune`
5. **Update Docker regularly:** Keep Docker Desktop updated

## Next Steps

Once you're comfortable with Docker basics:
1. Learn about Docker volumes for persistent data
2. Explore Docker networks for multi-container communication
3. Study Docker security best practices
4. Look into Docker in production (orchestration with Kubernetes)




