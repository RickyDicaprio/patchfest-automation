import pytest
import os
import tempfile
from pathlib import Path
from scripts.cleanup_temp import cleanup_directory, is_temp_file, main
import sys
from unittest.mock import patch

def test_is_temp_file():
    """Test temp file detection."""
    extensions = [".log", ".tmp", ".cache"]
    
    # Test extension matching
    assert is_temp_file("/path/to/debug.log", extensions) == True
    assert is_temp_file("/path/to/temp.tmp", extensions) == True
    assert is_temp_file("/path/to/cache.cache", extensions) == True
    assert is_temp_file("/path/to/important.txt", extensions) == False
    
    # Test special patterns
    assert is_temp_file("/path/to/.DS_Store", extensions) == True
    assert is_temp_file("/path/to/Thumbs.db", extensions) == True
    assert is_temp_file("/path/to/file.pyc", extensions) == True
    assert is_temp_file("/path/to/__pycache__/module.pyc", extensions) == True

def test_cleanup_directory_basic(tmp_path):
    """Test basic cleanup functionality."""
    # Create test files
    temp_dir = tmp_path / "test_cleanup"
    temp_dir.mkdir()
    
    # Create temp files to be removed
    (temp_dir / "debug.log").write_text("log content")
    (temp_dir / "temp.tmp").write_text("temp content")
    (temp_dir / "cache.cache").write_text("cache content")
    
    # Create file that should not be removed
    (temp_dir / "important.txt").write_text("important content")
    
    # Run cleanup
    extensions = [".log", ".tmp", ".cache"]
    found, deleted, errors = cleanup_directory(str(temp_dir), extensions, dry_run=False)
    
    # Check results
    assert found == 3
    assert deleted == 3
    assert errors == 0
    
    # Check that temp files are removed and important file remains
    assert not (temp_dir / "debug.log").exists()
    assert not (temp_dir / "temp.tmp").exists()
    assert not (temp_dir / "cache.cache").exists()
    assert (temp_dir / "important.txt").exists()

def test_cleanup_directory_dry_run(tmp_path):
    """Test dry run mode."""
    temp_dir = tmp_path / "test_dry_run"
    temp_dir.mkdir()
    
    # Create temp file
    temp_file = temp_dir / "debug.log"
    temp_file.write_text("log content")
    
    # Run dry run
    extensions = [".log"]
    found, deleted, errors = cleanup_directory(str(temp_dir), extensions, dry_run=True)
    
    # Check results - file should be found but not deleted
    assert found == 1
    assert deleted == 0
    assert errors == 0
    assert temp_file.exists()  # File should still exist

def test_cleanup_directory_nested(tmp_path):
    """Test cleanup in nested directories."""
    temp_dir = tmp_path / "test_nested"
    temp_dir.mkdir()
    
    # Create nested structure
    nested_dir = temp_dir / "subdir" / "deeper"
    nested_dir.mkdir(parents=True)
    
    # Create temp files in different levels
    (temp_dir / "root.log").write_text("content")
    (temp_dir / "subdir" / "sub.tmp").write_text("content") 
    (nested_dir / "deep.cache").write_text("content")
    
    # Run cleanup
    extensions = [".log", ".tmp", ".cache"]
    found, deleted, errors = cleanup_directory(str(temp_dir), extensions, dry_run=False)
    
    # All temp files should be found and deleted
    assert found == 3
    assert deleted == 3
    assert errors == 0

def test_cleanup_directory_nonexistent():
    """Test handling of nonexistent directory."""
    found, deleted, errors = cleanup_directory("/nonexistent/path", [".log"], dry_run=False)
    
    assert found == 0
    assert deleted == 0
    assert errors == 1

def test_cleanup_directory_permission_error(tmp_path, monkeypatch):
    """Test handling of permission errors."""
    temp_dir = tmp_path / "test_permission"
    temp_dir.mkdir()
    
    # Create a temp file
    temp_file = temp_dir / "debug.log"
    temp_file.write_text("content")
    
    # Mock os.remove to raise PermissionError
    def mock_remove(path):
        raise PermissionError("Permission denied")
    
    monkeypatch.setattr(os, "remove", mock_remove)
    
    # Run cleanup
    found, deleted, errors = cleanup_directory(str(temp_dir), [".log"], dry_run=False)
    
    assert found == 1
    assert deleted == 0
    assert errors == 1

def test_main_help():
    """Test main function help output."""
    with patch.object(sys, 'argv', ['cleanup_temp.py', '--help']):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code == 0

def test_main_single_directory(tmp_path, capsys):
    """Test main function with single directory."""
    temp_dir = tmp_path / "test_main"
    temp_dir.mkdir()
    
    # Create temp file
    (temp_dir / "test.log").write_text("content")
    
    with patch.object(sys, 'argv', ['cleanup_temp.py', str(temp_dir)]):
        main()
    
    # Check that file was deleted
    assert not (temp_dir / "test.log").exists()

def test_main_dry_run(tmp_path, capsys):
    """Test main function with dry run."""
    temp_dir = tmp_path / "test_main_dry"
    temp_dir.mkdir()
    
    # Create temp file
    temp_file = temp_dir / "test.log"
    temp_file.write_text("content")
    
    with patch.object(sys, 'argv', ['cleanup_temp.py', str(temp_dir), '--dry-run']):
        main()
    
    # Check that file still exists
    assert temp_file.exists()

def test_main_custom_extensions(tmp_path):
    """Test main function with custom extensions."""
    temp_dir = tmp_path / "test_main_ext"
    temp_dir.mkdir()
    
    # Create files with custom extensions
    (temp_dir / "test.custom").write_text("content")
    (temp_dir / "test.other").write_text("content")
    (temp_dir / "test.log").write_text("content")  # Default extension
    
    with patch.object(sys, 'argv', ['cleanup_temp.py', str(temp_dir), '--extensions', '.custom']):
        main()
    
    # Only .custom file should be deleted
    assert not (temp_dir / "test.custom").exists()
    assert (temp_dir / "test.other").exists()
    assert (temp_dir / "test.log").exists()  # Default extension not used

def test_main_multiple_directories(tmp_path):
    """Test main function with multiple directories."""
    dir1 = tmp_path / "dir1"
    dir2 = tmp_path / "dir2"
    dir1.mkdir()
    dir2.mkdir()
    
    # Create temp files in both directories
    (dir1 / "test1.log").write_text("content")
    (dir2 / "test2.tmp").write_text("content")
    
    with patch.object(sys, 'argv', ['cleanup_temp.py', str(dir1), str(dir2)]):
        main()
    
    # Both files should be deleted
    assert not (dir1 / "test1.log").exists()
    assert not (dir2 / "test2.tmp").exists()