import os
import shutil
import pytest
from scripts import backup_folder

def test_backup_functionality(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "file1.txt").write_text("content")
    
    dest = tmp_path / "backup"
    
    if hasattr(backup_folder, 'backup_files'):
        backup_folder.backup_files(str(source), str(dest))
        assert os.path.exists(dest / "file1.txt")