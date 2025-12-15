import pytest
import os
import zipfile
from pathlib import Path
from scripts.backup_folder import (
    backup_folder, 
    calculate_folder_size,
    format_size,
    get_backup_name,
    verify_backup,
    main
)
import sys
from unittest.mock import patch

def test_backup_folder_creates_destination(tmp_path):
    """Test basic backup functionality."""
    src = tmp_path / "source"
    dst = tmp_path / "backup"
    src.mkdir()

    result = backup_folder(str(src), str(dst))
    
    assert result == True
    assert dst.exists()

def test_backup_folder_copies_files(tmp_path):
    """Test file copying functionality."""
    src = tmp_path / "source"
    dst = tmp_path / "backup"
    src.mkdir()
    
    # Create test file
    file = src / "test.txt"
    file.write_text("hello world")
    
    result = backup_folder(str(src), str(dst))
    
    assert result == True
    copied_file = dst / "test.txt"
    assert copied_file.exists()
    assert copied_file.read_text() == "hello world"

def test_backup_folder_copies_nested_structure(tmp_path):
    """Test nested directory structure copying."""
    src = tmp_path / "source"
    dst = tmp_path / "backup"
    src.mkdir()
    
    # Create nested structure
    nested_dir = src / "subdir" / "deep"
    nested_dir.mkdir(parents=True)
    
    # Create files at different levels
    (src / "root.txt").write_text("root content")
    (src / "subdir" / "sub.txt").write_text("sub content")
    (nested_dir / "deep.txt").write_text("deep content")
    
    result = backup_folder(str(src), str(dst))
    
    assert result == True
    assert (dst / "root.txt").read_text() == "root content"
    assert (dst / "subdir" / "sub.txt").read_text() == "sub content"
    assert (dst / "subdir" / "deep" / "deep.txt").read_text() == "deep content"

def test_backup_folder_compressed(tmp_path):
    """Test compressed backup functionality."""
    src = tmp_path / "source"
    dst = tmp_path / "backup.zip"
    src.mkdir()
    
    # Create test files
    (src / "file1.txt").write_text("content 1")
    (src / "file2.txt").write_text("content 2")
    
    result = backup_folder(str(src), str(dst), compress=True)
    
    assert result == True
    assert dst.exists()

def test_backup_folder_nonexistent_source(tmp_path):
    """Test handling of nonexistent source folder."""
    src = tmp_path / "nonexistent"
    dst = tmp_path / "backup"
    
    result = backup_folder(str(src), str(dst))
    
    assert result == False

def test_backup_folder_with_verification(tmp_path):
    """Test backup with verification enabled."""
    src = tmp_path / "source"
    dst = tmp_path / "backup"
    src.mkdir()
    
    (src / "test.txt").write_text("test content")
    
    result = backup_folder(str(src), str(dst), verify=True)
    
    assert result == True
    assert dst.exists()
    assert (dst / "test.txt").exists()

def test_calculate_folder_size(tmp_path):
    """Test folder size calculation."""
    test_dir = tmp_path / "test"
    test_dir.mkdir()
    
    # Create files with known sizes
    (test_dir / "small.txt").write_text("12345")  # 5 bytes
    (test_dir / "large.txt").write_text("x" * 1000)  # 1000 bytes
    
    size = calculate_folder_size(test_dir)
    assert size >= 1005  # At least 1005 bytes

def test_format_size():
    """Test size formatting function."""
    assert format_size(0) == "0B"
    assert format_size(512) == "512.00B"
    assert format_size(1024) == "1.00KB"
    assert format_size(1024 * 1024) == "1.00MB"
    assert format_size(1536) == "1.50KB"

def test_get_backup_name():
    """Test backup name generation."""
    # Test uncompressed backup name
    name = get_backup_name("/path/to/folder", compressed=False)
    assert "folder_backup_" in name
    assert not name.endswith(".zip")
    
    # Test compressed backup name
    name = get_backup_name("/path/to/folder", compressed=True)
    assert "folder_backup_" in name
    assert name.endswith(".zip")
