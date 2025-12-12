import os
import shutil
from src.backup import backup_folder

def test_backup_folder_creates_destination(tmp_path):
    src = tmp_path / "source"
    dst = tmp_path / "backup"
    src.mkdir()

    backup_folder(str(src), str(dst))

    assert dst.exists()

def test_backup_folder_copies_files(tmp_path):
    src = tmp_path / "source"
    dst = tmp_path / "backup"
    src.mkdir()
    file = src / "test.txt"
    file.write_text("hello")

    backup_folder(str(src), str(dst))

    copied_file = dst / "test.txt"
    assert copied_file.exists()
    assert copied_file.read_text() == "hello"
def backup_folder(src, dst):
    # BUG: doesn't actually copy anything
    print(f"Backup from {src} to {dst}, but not doing it :)")
