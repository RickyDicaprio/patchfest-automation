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

### Cleanup Temp Script
The cleanup script safely removes temporary files from specified directories:

**Basic usage:**
```bash
# Clean current directory
python scripts/cleanup_temp.py .

# Clean specific directory
python scripts/cleanup_temp.py /path/to/directory

# Clean multiple directories
python scripts/cleanup_temp.py /tmp /var/log ~/Downloads
```

**Dry-run mode (preview files without deleting):**
```bash
# See what would be deleted
python scripts/cleanup_temp.py /path/to/directory --dry-run
```

**Custom file extensions:**
```bash
# Only remove .log and .tmp files
python scripts/cleanup_temp.py /path/to/directory --extensions .log .tmp

# Remove backup files
python scripts/cleanup_temp.py . --extensions .bak .old .backup
```

**Verbose output:**
```bash
# Get detailed logging
python scripts/cleanup_temp.py /tmp --verbose --dry-run
```

**Default file types removed:**
- `.log` - Log files
- `.tmp` - Temporary files  
- `.cache` - Cache files
- `.bak` - Backup files
- `.swp` - Swap files
- `*~` - Editor backup files
- `.DS_Store` - macOS metadata
- `Thumbs.db` - Windows thumbnails
- `.pyc` - Python bytecode
- `__pycache__` - Python cache directories

