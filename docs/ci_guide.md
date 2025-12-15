
# CI Guide

## Overview
This project uses Continuous Integration (CI) to ensure code quality and consistency. The CI system automatically runs formatting, linting, and testing checks on every pull request and push to the main branch.

**Tools used:**
- GitHub Actions for automated CI/CD
- Black for Python code formatting
- Flake8 for Python linting
- Pytest for running unit tests

## CI Workflow Diagram
```
Pull Request Created
        ↓
┌─────────────────┐
│   Format Check  │ ← ./ci/format.sh
│   (black)       │
└─────────────────┘
        ↓
┌─────────────────┐
│   Lint Check    │ ← ./ci/lint.sh  
│   (flake8)      │
└─────────────────┘
        ↓
┌─────────────────┐
│   Run Tests     │ ← ./ci/run_tests.sh
│   (pytest)      │
└─────────────────┘
        ↓
┌─────────────────┐
│   All Checks    │
│   Pass? ✅      │
└─────────────────┘
        ↓
    Merge Ready!
```

## CI Scripts Explained

### 1. format.sh - Code Formatting
**Purpose:** Automatically formats Python code using Black formatter
**What it does:**
- Checks if Black is installed
- Runs `black .` to format all Python files
- Ensures consistent code style across the project

**Usage:**
```bash
chmod +x ci/format.sh
./ci/format.sh
```

### 2. lint.sh - Code Linting  
**Purpose:** Checks Python code for style issues and potential errors using Flake8
**What it does:**
- Checks if Flake8 is installed
- Runs `flake8 .` to analyze all Python files
- Reports style violations and potential issues

**Usage:**
```bash
chmod +x ci/lint.sh
./ci/lint.sh
```

### 3. run_tests.sh - Test Execution
**Purpose:** Runs all unit tests using Pytest
**What it does:**
- Checks if Pytest is installed  
- Runs `pytest -q` to execute all tests
- Reports test results and failures

**Usage:**
```bash
chmod +x ci/run_tests.sh
./ci/run_tests.sh
```

## Running CI Checks Locally

Before creating a pull request, run all CI checks locally:

### Prerequisites
Install required tools:
```bash
pip install -r requirements.txt
pip install black flake8 pytest
```

### Step-by-Step Local CI Process

1. **Format your code:**
   ```bash
   ./ci/format.sh
   ```

2. **Check for lint issues:**
   ```bash
   ./ci/lint.sh
   ```

3. **Run all tests:**
   ```bash
   ./ci/run_tests.sh
   ```

4. **Run all checks at once:**
   ```bash
   ./ci/format.sh && ./ci/lint.sh && ./ci/run_tests.sh
   ```

### Fixing Common Issues

**Black formatting errors:**
- Black automatically fixes formatting - just run `./ci/format.sh` again

**Flake8 lint errors:**
- Fix manually based on error messages
- Common issues: line too long, unused imports, missing docstrings

**Test failures:**
- Check test output for specific failure details
- Run individual tests: `pytest tests/test_specific.py -v`

## GitHub Actions Integration

The CI process is automated through GitHub Actions in `.github/workflows/main-ci.yml`.

**Triggers:**
- Every push to `main` branch
- Every pull request to `main` branch

**Jobs:**
- **build-test:** Sets up Python 3.11, installs dependencies, runs tests and linting

**Workflow steps:**
1. Checkout repository code
2. Setup Python 3.11 environment
3. Install dependencies from requirements.txt
4. Run pytest tests
5. Run lint checks
6. Report results

## Best Practices for Contributors

1. **Before committing:**
   - Run `./ci/format.sh` to auto-format code
   - Run `./ci/lint.sh` to check for style issues
   - Run `./ci/run_tests.sh` to ensure tests pass

2. **Pull Request Guidelines:**
   - Ensure all CI checks pass (green checkmarks)
   - Fix any failing tests or lint issues
   - Add tests for new functionality

3. **Debugging CI Failures:**
   - Check the Actions tab on GitHub for detailed logs
   - Run the same commands locally to reproduce issues
   - Use `pytest -v` for verbose test output

## Troubleshooting

**Permission denied errors:**
```bash
chmod +x ci/format.sh ci/lint.sh ci/run_tests.sh
```

**Missing dependencies:**
```bash
pip install -r requirements.txt
pip install black flake8 pytest
```

**PYTHONPATH issues:**
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest
```

    # Adding New CI Jobs
        --> How to create or modify CI workflows.

    # Troubleshooting CI Failures
        --> Reading logs.
        --> Common errors and solutions.

    # Best Practices
        --> Caching dependencies.
        --> Keeping pipelines fast.

