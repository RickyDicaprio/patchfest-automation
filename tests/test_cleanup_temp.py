import pytest
import os
import tempfile
from scripts.cleanup_temp import cleanup, TEMP_EXTENSIONS

def test_cleanup_removes_temp_files(tmp_path):
    # Create a temp directory with some files
    temp_dir = tmp_path / "test_dir"
    temp_dir.mkdir()
    
    # Create temp files to be removed
    temp_file1 = temp_dir / "debug.log"
    temp_file1.write_text("log content")
    
    temp_file2 = temp_dir / "temp.tmp"
    temp_file2.write_text("temp content")
    
    # Create a file that should not be removed
    keep_file = temp_dir / "important.txt"
    keep_file.write_text("keep this")
    
    # Run cleanup
    cleanup(str(temp_dir))
    
    # Check that temp files are removed
    assert not temp_file1.exists()
    assert not temp_file2.exists()
    
    # Check that non-temp file remains
    assert keep_file.exists()

def test_cleanup_handles_nested_directories(tmp_path):
    # Create nested structure
    parent_dir = tmp_path / "parent"
    parent_dir.mkdir()
    child_dir = parent_dir / "child"
    child_dir.mkdir()
    
    # Temp file in child dir
    temp_file = child_dir / "nested.cache"
    temp_file.write_text("nested temp")
    
    cleanup(str(parent_dir))
    
    assert not temp_file.exists()

def test_cleanup_with_no_temp_files(tmp_path):
    temp_dir = tmp_path / "empty_dir"
    temp_dir.mkdir()
    
    # Should not error
    cleanup(str(temp_dir))
    
    assert temp_dir.exists()

def test_temp_extensions_list():
    # Ensure the extensions are as expected
    expected = [".log", ".tmp", ".cache"]
    assert TEMP_EXTENSIONS == expected