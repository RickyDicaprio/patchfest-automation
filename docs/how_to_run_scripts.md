# How to Run Scripts

## Prerequisites
- Required software (Python, Node, Bash, Docker, etc.)
- Environment variables that must be set.

## Script Directory Structure
See `scripts/README.md` for a detailed overview of all scripts and their purposes.

## Creating New Scripts

To create a new automation script, use the provided template:

1. Copy `templates/automation_script_template.py` to `scripts/your_script_name.py`
2. Customize the script with your logic, following the naming convention (snake_case).
3. Add a short comment at the top explaining the script's purpose.
4. Update `scripts/README.md` to document the new script.

The template includes:
- Command-line argument parsing with `argparse`
- Logging setup for info and error messages
- Sample `main()` function structure
- Error handling examples

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

## Troubleshooting
- Common errors and fixes.

## Examples
- Practical examples of typical script runs.

### Example: Running the Sample Hello Script
```bash
python scripts/sample_hello.py
```
Output:
```
🚀 Automation Script Running Successfully!
Current Time: 2025-12-15 12:00:00.000000
```

### Example: Running the System Info Script
```bash
./scripts/system_info.sh
```
Output:
```
===============================
      SYSTEM INFORMATION
===============================
Hostname: your-hostname
...
```

