#!/usr/bin/env python3
"""
Temporary File Cleanup Script

Automatically removes temporary files from specified directories to keep the system organized.
Supports multiple target directories, dry-run mode, and comprehensive logging.

Features:
- Command-line argument parsing
- Dry-run mode to preview files before deletion
- Comprehensive logging
- Support for multiple directories
- Configurable file extensions
- Error handling and reporting

Usage:
    python scripts/cleanup_temp.py --help
    python scripts/cleanup_temp.py /path/to/directory
    python scripts/cleanup_temp.py /path1 /path2 --dry-run
    python scripts/cleanup_temp.py /path --extensions .log .tmp .cache
"""

import argparse
import logging
import os
import sys
from pathlib import Path

# Default temporary file extensions
DEFAULT_TEMP_EXTENSIONS = [".log", ".tmp", ".cache", ".bak", ".swp", ".~"]

# Common temporary file patterns
TEMP_PATTERNS = [
    "*.log",
    "*.tmp",
    "*.cache",
    "*.bak", 
    "*.swp",
    "*~",
    ".DS_Store",
    "Thumbs.db",
    "*.pyc",
    "__pycache__"
]

def setup_logging(verbose=False):
    """
    Set up logging configuration.
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout
    )

def is_temp_file(filepath, extensions):
    """
    Check if a file should be considered a temporary file.
    """
    filename = os.path.basename(filepath)
    
    # Check extensions
    for ext in extensions:
        if filename.endswith(ext):
            return True
    
    # Check special patterns
    if filename in [".DS_Store", "Thumbs.db"]:
        return True
    
    # Check for hidden backup files
    if filename.startswith(".") and filename.endswith("~"):
        return True
    
    # Check for Python cache
    if "__pycache__" in filepath or filename.endswith(".pyc"):
        return True
    
    return False

def cleanup_directory(directory, extensions, dry_run=False):
    """
    Clean temporary files from a single directory.
    
    Args:
        directory (str): Path to directory to clean
        extensions (list): List of file extensions to remove
        dry_run (bool): If True, only preview files without deleting
    
    Returns:
        tuple: (files_found, files_deleted, errors)
    """
    directory_path = Path(directory)
    
    if not directory_path.exists():
        logging.error(f"Directory does not exist: {directory}")
        return 0, 0, 1
    
    if not directory_path.is_dir():
        logging.error(f"Path is not a directory: {directory}")
        return 0, 0, 1
    
    files_found = 0
    files_deleted = 0
    errors = 0
    
    logging.info(f"{'[DRY RUN] ' if dry_run else ''}Scanning directory: {directory}")
    
    try:
        for root, dirs, files in os.walk(directory):
            # Skip hidden directories like .git
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                filepath = os.path.join(root, filename)
                
                if is_temp_file(filepath, extensions):
                    files_found += 1
                    
                    if dry_run:
                        logging.info(f"[WOULD DELETE] {filepath}")
                    else:
                        try:
                            os.remove(filepath)
                            files_deleted += 1
                            logging.info(f"Deleted: {filepath}")
                        except OSError as e:
                            errors += 1
                            logging.error(f"Failed to delete {filepath}: {e}")
                        except Exception as e:
                            errors += 1
                            logging.error(f"Unexpected error deleting {filepath}: {e}")
    
    except PermissionError as e:
        logging.error(f"Permission denied accessing {directory}: {e}")
        errors += 1
    except Exception as e:
        logging.error(f"Unexpected error scanning {directory}: {e}")
        errors += 1
    
    return files_found, files_deleted, errors

def main():
    """
    Main function that parses arguments and runs the cleanup.
    """
    parser = argparse.ArgumentParser(
        description='Clean temporary files from specified directories',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/cleanup_temp.py /tmp
  python scripts/cleanup_temp.py /home/user/Downloads --dry-run
  python scripts/cleanup_temp.py /var/log /tmp --extensions .log .tmp
  python scripts/cleanup_temp.py . --verbose --dry-run
        """
    )
    
    parser.add_argument(
        'directories',
        nargs='+',
        help='One or more directories to clean'
    )
    
    parser.add_argument(
        '--extensions',
        nargs='+',
        default=DEFAULT_TEMP_EXTENSIONS,
        help=f'File extensions to remove (default: {" ".join(DEFAULT_TEMP_EXTENSIONS)})'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview files that would be deleted without actually deleting them'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true', 
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Set up logging
    setup_logging(args.verbose)
    
    if args.dry_run:
        logging.info("🔍 DRY RUN MODE: Files will be listed but not deleted")
    
    total_found = 0
    total_deleted = 0
    total_errors = 0
    
    # Process each directory
    for directory in args.directories:
        found, deleted, errors = cleanup_directory(
            directory, 
            args.extensions, 
            args.dry_run
        )
        total_found += found
        total_deleted += deleted
        total_errors += errors
    
    # Summary
    logging.info("\n" + "=" * 50)
    if args.dry_run:
        logging.info(f"📋 SUMMARY (DRY RUN):")
        logging.info(f"   Files that would be deleted: {total_found}")
    else:
        logging.info(f"✅ CLEANUP SUMMARY:")
        logging.info(f"   Files found: {total_found}")
        logging.info(f"   Files deleted: {total_deleted}")
    
    if total_errors > 0:
        logging.warning(f"   Errors encountered: {total_errors}")
    
    logging.info("=" * 50)
    
    # Exit with error code if there were errors
    if total_errors > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
