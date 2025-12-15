# How to Run Scripts

## Prerequisites
- Required software (Python, Node, Bash, Docker, etc.)
- Environment variables that must be set.

## Script Directory Structure
- Overview of /scripts/* and what each script does.

## Running Scripts

### Running Shell Scripts
./scripts/script_name.sh

### Running Python Scripts
python scripts/script_name.py --options

### Running Node Scripts
npm run script_name



## Passing Arguments
- Examples of using flags or parameters.

## Environment Setup
- How to configure environment variables or .env files.

## Running Tests

Before submitting a PR, run the test suite to ensure your scripts work correctly:

```bash
./ci/run_tests.sh
```

This will run all unit tests using pytest. Make sure pytest is installed (`pip install -r requirements.txt`).

### Writing Tests

- Add test files in `tests/` with the naming pattern `test_<script_name>.py`
- Use pytest fixtures for temporary directories and files
- Test both success and error cases

## Troubleshooting
- Common errors and fixes.

## Examples
- Practical examples of typical script runs.

