#!/usr/bin/env python3
"""
Backup any folder into a timestamped ZIP archive.
"""

import os
import sys
import shutil
from datetime import datetime

def backup(source_folder):
    if not os.path.exists(source_folder):
        print("❌ Folder does not exist.")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    
    shutil.make_archive(f"backup_{timestamp}", "zip", source_folder)
    
    print(f"✔ Backup created: {backup_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python backup_folder.py <folder_to_backup>")
        sys.exit(1)

    backup(sys.argv[1])
