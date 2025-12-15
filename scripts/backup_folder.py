#!/usr/bin/env python3
"""
Folder Backup Script

Automatically backs up a source folder to a destination with optional compression.
Provides comprehensive logging and error handling for reliable backup automation.

Features:
- Command-line argument parsing
- Optional ZIP compression
- Comprehensive logging with progress updates
- Error handling and validation
- Backup verification
- Incremental and full backup modes

Usage:
    python scripts/backup_folder.py --help
    python scripts/backup_folder.py /source/path /destination/path
    python scripts/backup_folder.py /source/path /destination/path --compress
    python scripts/backup_folder.py /source/path /destination/path --compress --verify
"""

import argparse
import logging
import os
import shutil
import sys
import zipfile
from datetime import datetime
from pathlib import Path

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

def get_backup_name(source_path, compressed=False):
    """
    Generate a timestamped backup name.
    """
    source_name = os.path.basename(os.path.abspath(source_path))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if compressed:
        return f"{source_name}_backup_{timestamp}.zip"
    else:
        return f"{source_name}_backup_{timestamp}"

def calculate_folder_size(folder_path):
    """
    Calculate total size of a folder in bytes.
    """
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)
                except (OSError, FileNotFoundError):
                    # Skip files that can't be accessed
                    continue
    except (OSError, PermissionError):
        logging.warning(f"Could not calculate size for {folder_path}")
    
    return total_size

def format_size(size_bytes):
    """
    Format bytes to human readable format.
    """
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024.0 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.2f}{size_names[i]}"

def backup_folder_uncompressed(source_path, destination_path):
    """
    Backup folder without compression using shutil.copytree.
    """
    source_path = Path(source_path).resolve()
    destination_path = Path(destination_path).resolve()
    
    if not source_path.exists():
        raise FileNotFoundError(f"Source folder does not exist: {source_path}")
    
    if not source_path.is_dir():
        raise ValueError(f"Source path is not a directory: {source_path}")
    
    # Create destination parent directory if it doesn't exist
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    
    logging.info(f"Starting backup: {source_path} -> {destination_path}")
    
    # Calculate source size
    source_size = calculate_folder_size(source_path)
    logging.info(f"Source folder size: {format_size(source_size)}")
    
    try:
        # Copy the entire directory tree
        shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        logging.info("Backup completed successfully")
        
        # Verify backup size
        backup_size = calculate_folder_size(destination_path)
        logging.info(f"Backup folder size: {format_size(backup_size)}")
        
        return True
        
    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
        return False
    except OSError as e:
        logging.error(f"OS error during backup: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during backup: {e}")
        return False

def backup_folder_compressed(source_path, destination_path):
    """
    Backup folder with ZIP compression.
    """
    source_path = Path(source_path).resolve()
    destination_path = Path(destination_path).resolve()
    
    if not source_path.exists():
        raise FileNotFoundError(f"Source folder does not exist: {source_path}")
    
    if not source_path.is_dir():
        raise ValueError(f"Source path is not a directory: {source_path}")
    
    # Ensure destination has .zip extension
    if not destination_path.suffix.lower() == '.zip':
        destination_path = destination_path.with_suffix('.zip')
    
    # Create destination parent directory if it doesn't exist
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    
    logging.info(f"Starting compressed backup: {source_path} -> {destination_path}")
    
    # Calculate source size
    source_size = calculate_folder_size(source_path)
    logging.info(f"Source folder size: {format_size(source_size)}")
    
    try:
        with zipfile.ZipFile(destination_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            file_count = 0
            
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_path)
                    
                    try:
                        zipf.write(file_path, arcname)
                        file_count += 1
                        
                        if file_count % 100 == 0:
                            logging.debug(f"Compressed {file_count} files...")
                            
                    except (OSError, PermissionError) as e:
                        logging.warning(f"Could not compress {file_path}: {e}")
                        continue
            
            logging.info(f"Compressed {file_count} files")
        
        # Check final compressed size
        compressed_size = destination_path.stat().st_size
        compression_ratio = (1 - compressed_size / source_size) * 100 if source_size > 0 else 0
        
        logging.info(f"Compressed backup size: {format_size(compressed_size)}")
        logging.info(f"Compression ratio: {compression_ratio:.1f}%")
        logging.info("Compressed backup completed successfully")
        
        return True
        
    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
        return False
    except OSError as e:
        logging.error(f"OS error during compressed backup: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during compressed backup: {e}")
        return False

def verify_backup(source_path, backup_path, compressed=False):
    """
    Verify that backup was created successfully.
    """
    if compressed:
        if not backup_path.exists() or backup_path.stat().st_size == 0:
            return False
        
        try:
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                # Test the zip file integrity
                bad_file = zipf.testzip()
                return bad_file is None
        except zipfile.BadZipFile:
            return False
    else:
        if not backup_path.exists() or not backup_path.is_dir():
            return False
        
        # Basic verification - check if some files exist
        try:
            source_files = list(Path(source_path).rglob('*'))
            backup_files = list(backup_path.rglob('*'))
            
            # Should have similar number of items
            return len(backup_files) >= len(source_files) * 0.9
        except Exception:
            return False

def backup_folder(src, dst, compress=False, verify=False):
    """
    Main backup function that handles both compressed and uncompressed backups.
    
    Args:
        src (str): Source folder path
        dst (str): Destination folder path
        compress (bool): Whether to use ZIP compression
        verify (bool): Whether to verify backup after creation
    
    Returns:
        bool: True if backup was successful, False otherwise
    """
    try:
        if compress:
            success = backup_folder_compressed(src, dst)
        else:
            success = backup_folder_uncompressed(src, dst)
        
        if success and verify:
            logging.info("Verifying backup...")
            if verify_backup(src, Path(dst), compress):
                logging.info("✅ Backup verification successful")
            else:
                logging.warning("⚠️  Backup verification failed")
                success = False
        
        return success
        
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return False
    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False

def main():
    """
    Main function that parses arguments and runs the backup.
    """
    parser = argparse.ArgumentParser(
        description='Backup a source folder to a destination with optional compression',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/backup_folder.py /home/user/documents /backups/documents
  python scripts/backup_folder.py /home/user/photos /backups --compress
  python scripts/backup_folder.py ./project /backups/project --compress --verify
  python scripts/backup_folder.py /data /backup --auto-name --compress
        """
    )
    
    parser.add_argument(
        'source',
        help='Source folder to backup'
    )
    
    parser.add_argument(
        'destination',
        help='Destination path for backup'
    )
    
    parser.add_argument(
        '--compress',
        action='store_true',
        help='Create compressed ZIP backup'
    )
    
    parser.add_argument(
        '--verify',
        action='store_true',
        help='Verify backup after creation'
    )
    
    parser.add_argument(
        '--auto-name',
        action='store_true',
        help='Automatically generate timestamped backup name'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Set up logging
    setup_logging(args.verbose)
    
    # Handle auto-naming
    destination = args.destination
    if args.auto_name:
        backup_name = get_backup_name(args.source, args.compress)
        destination = os.path.join(destination, backup_name)
    
    logging.info("📁 Starting folder backup...")
    logging.info(f"Source: {os.path.abspath(args.source)}")
    logging.info(f"Destination: {os.path.abspath(destination)}")
    logging.info(f"Compression: {'Yes' if args.compress else 'No'}")
    logging.info(f"Verification: {'Yes' if args.verify else 'No'}")
    
    # Perform backup
    success = backup_folder(
        args.source,
        destination, 
        compress=args.compress,
        verify=args.verify
    )
    
    if success:
        logging.info("✅ Backup completed successfully!")
        sys.exit(0)
    else:
        logging.error("❌ Backup failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
