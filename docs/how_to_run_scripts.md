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

### Backup Folder Script
The backup script automatically backs up folders with optional compression:

**Basic folder backup:**
```bash
# Simple folder backup
python scripts/backup_folder.py /source/folder /backup/destination

# Backup documents to external drive
python scripts/backup_folder.py ~/Documents /media/external/backups
```

**Compressed backup with ZIP:**
```bash
# Create compressed backup
python scripts/backup_folder.py /source/folder /backup/backup.zip --compress

# Compress and verify backup
python scripts/backup_folder.py /important/data /backups/data.zip --compress --verify
```

**Auto-named backups with timestamps:**
```bash
# Generate timestamped backup name automatically
python scripts/backup_folder.py /project /backups --auto-name

# Compressed auto-named backup
python scripts/backup_folder.py /project /backups --auto-name --compress
```

**Advanced usage:**
```bash
# Verbose output with verification
python scripts/backup_folder.py /data /backup --verbose --verify

# Full-featured backup
python scripts/backup_folder.py ~/Pictures ~/backups/photos --compress --auto-name --verify --verbose
```

**Features:**
- Preserves file permissions and timestamps
- Creates parent directories automatically
- Provides progress logging and size information
- Supports verification of backup integrity
- Handles nested directory structures
- Compression ratios shown for ZIP backups
- Timestamped backup names to prevent overwrites

