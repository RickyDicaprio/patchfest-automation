# PatchFest Automations

Welcome to PatchFest Automations! This repository contains small automation scripts, GitHub Actions samples, Docker setups, CI helper tools, templates, and intentionally buggy code designed for contributors to patch during PatchFest.

## Repository Structure
scripts/ → Python + Bash automation scripts
actions/ → GitHub Actions workflow samples
docker/ → Dockerfiles & Docker Compose examples
ci/ → Linter, formatter, and CI support scripts
templates/ → CLI and automation templates
tests/ → Unit tests revealing bugs
docs/ → Guides and documentation
.github/ → Issue templates & CI configuration


## How to Contribute (Fork → Branch → PR)

1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b fix/<short-description>
3. Make your changes. Good PatchFest contributions include:
   -> Fixing failing tests
   -> Patching buggy automation scripts
   -> Improving GitHub Actions workflows
   -> Enhancing Docker configurations
   -> Updating CI support scripts
   -> Improving or extending templates
   -> Adding missing documentation
4. Run tests
   pytest -v
5. Commit your changes
   git add .
   git commit -m "fix: <short description>"
6. Push your branch and open a Pull Request.

## Where to Start (Bug Locations)

# Intentional bugs and tasks can be found across the repository:
   scripts/ — broken automation logic in Python/Bash
   actions/ — incomplete or failing GitHub Actions examples
   docker/ — Dockerfiles needing fixes or optimizations
   ci/ — formatting/lint helpers with issues
   templates/ — CLI scaffolds needing improvements
   tests/ — unit tests designed to fail until patched
   
Use the tests in the tests/ directory to guide your fixes.

# Documentation
Detailed guides are provided in the docs/ directory:
   -> [Docker Guide](docs/docker_guide.md) - Complete Docker setup and usage guide for beginners
   -> [Automation Overview](docs/automation_overview.md) - High-level overview of the automation framework
   -> [How to Run Scripts](docs/how_to_run_scripts.md) - Detailed guide for executing automation scripts
   -> [CI Pipeline Documentation](docs/ci_guide.md) - Setting up and understanding CI/CD workflows

# Using Docker
If your patch involves Docker automation:
   docker build -t patchfest .
   docker run -it patchfest


# Contribution Rules
   -> Keep patches small and focuseds
   -> Fix one issue per pull requests
   -> Follow existing coding conventionss
   -> Do not break the CI workflows
   -> Update documentation when modifying behaviors