# Docker Guide

## Introduction
This project uses Docker to provide a consistent and isolated environment for running automation scripts. Contributors don't need to install Python or packages locally - everything runs inside containers.

## Prerequisites
- Install Docker & Docker Compose from https://docs.docker.com/get-docker/

## Project Structure
- `docker/Dockerfile`: Defines the Python environment with all dependencies
- `docker/docker-compose.yml`: Orchestrates container setup with volume mounts
- `docker/entrypoint.sh`: Entry point script for running automation scripts

## Building and Running

### Quick Start
```bash
# Build and run the container
docker-compose -f docker/docker-compose.yml up --build

# Run a specific script
docker-compose -f docker/docker-compose.yml run automation_scripts python scripts/backup_folder.py --help
```

### Running Individual Scripts
```bash
# Run backup script
docker-compose -f docker/docker-compose.yml run automation_scripts python scripts/backup_folder.py /source /destination

# Run cleanup script  
docker-compose -f docker/docker-compose.yml run automation_scripts python scripts/cleanup_temp.py /path/to/directory

# Run sample hello script
docker-compose -f docker/docker-compose.yml run automation_scripts python scripts/sample_hello.py
```

### Running Tests
```bash
# Run all tests
docker-compose -f docker/docker-compose.yml run automation_scripts ./ci/run_tests.sh

# Run specific test
docker-compose -f docker/docker-compose.yml run automation_scripts pytest tests/test_backup_folder.py
```

## Development Workflow
1. Write your script in `scripts/` directory
2. Test locally: `docker-compose -f docker/docker-compose.yml run automation_scripts python scripts/your_script.py`
3. Add tests in `tests/` directory
4. Run tests: `docker-compose -f docker/docker-compose.yml run automation_scripts ./ci/run_tests.sh`

## Volume Mounts
The container automatically mounts:
- `scripts/` → `/app/scripts` (your automation scripts)
- `tests/` → `/app/tests` (unit tests)
- `templates/` → `/app/templates` (script templates)

## Debugging
- View container logs: `docker-compose -f docker/docker-compose.yml logs`
- Interactive shell: `docker-compose -f docker/docker-compose.yml run automation_scripts bash`
- Clean up: `docker-compose -f docker/docker-compose.yml down`
    --> Exec into a running container:
        ```bash
        docker exec -it container-name /bin/sh
# Best Practices
    --> Keeping images small.
    --> Using .dockerignore.




