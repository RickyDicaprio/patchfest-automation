import os
import shutil

def backup_folder(src, dst):
    """
    Copy all files and folders from src to dst.
    """
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)

    if not os.path.exists(src):
        raise FileNotFoundError(f"Source folder does not exist: {src}")

    if not os.path.exists(dst):
        os.makedirs(dst)

    # Copy all files and subfolders
    for item in os.listdir(src):
        s_item = os.path.join(src, item)
        d_item = os.path.join(dst, item)
        if os.path.isdir(s_item):
            shutil.copytree(s_item, d_item, dirs_exist_ok=True)
        else:
            shutil.copy2(s_item, d_item)
