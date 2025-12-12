#!/usr/bin/env python3
"""
Automatically removes temporary files like .log, .tmp, and cache files
from a target directory.
"""

import os
import sys

TEMP_EXTENSIONS = [".log", ".tmp", ".cache"]

def cleanup(directory):
    removed = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in TEMP_EXTENSIONS):
                filepath = os.path.join(root, file)
                os.remove(filepath)
                removed += 1
                print(f"Deleted: {filepath}")

    print(f"\n✔ Total files deleted: {removed}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cleanup_temp.py <directory>")
        sys.exit(1)

    cleanup(sys.argv[1])
