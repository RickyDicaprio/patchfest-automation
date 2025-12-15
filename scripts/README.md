# Scripts Directory

This directory contains all automation scripts for the PatchFest Automation project.

## Organization

- **Python Scripts**: `.py` files for Python-based automation tasks.
- **Shell Scripts**: `.sh` files for shell-based automation tasks.
- **__init__.py**: Marks this directory as a Python package (if needed).

## Naming Convention

- Use `snake_case` for script names (e.g., `backup_folder.py`).
- Prefix with descriptive words indicating the script's purpose.
- Avoid spaces or special characters in filenames.

## Adding New Scripts

1. Copy `templates/automation_script_template.py` to this directory.
2. Rename it to a descriptive name following the naming convention.
3. Customize the script with your automation logic.
4. Add a short comment at the top explaining what the script does.
5. Test the script and update documentation if needed.

## Existing Scripts

- `backup_folder.py`: Backs up files and folders from a source to a destination directory.
- `cleanup_temp.py`: Removes temporary files (.log, .tmp, .cache) from a specified directory.
- `sample_hello.py`: A sample script that prints a hello message with current time.
- `system_info.sh`: Displays system information like hostname, user, OS, and memory usage.

## Usage

Run scripts from the project root:

```bash
python scripts/script_name.py [arguments]
./scripts/script_name.sh [arguments]
```

Refer to `docs/how_to_run_scripts.md` for detailed usage examples.