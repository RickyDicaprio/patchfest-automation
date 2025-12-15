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

## Troubleshooting
- Common errors and fixes.

## Examples
- Practical examples of typical script runs.

### System Information Scripts
We provide two versions of the system information script:

**Shell version (cross-platform compatible):**
```bash
./scripts/system_info.sh
```
Output:
```
🖥️  Operating System:
   OS: macOS 14.1
   Build: 23B74
   Architecture: arm64

🔧 CPU Information:  
   Model: Apple M1 Pro
   Cores: 10

💾 Memory Information:
   Total RAM: 32GB
   Used RAM: 12GB
   Available RAM: 20GB
...
```

**Python version (with JSON output option):**
```bash
# Text output (default)
python scripts/system_info.py

# JSON output for automation
python scripts/system_info.py --format json

# Save to file
python scripts/system_info.py --output system_report.txt
```

Both scripts display:
- Operating system name and version
- CPU model and core count  
- Memory usage (total, used, available)
- Disk usage for main partitions
- Additional system details

