import os
import pytest
from scripts import cleanup_temp

def test_cleanup_files(tmp_path):
    p = tmp_path / "test.tmp"
    p.write_text("temporary data")
    
    assert os.path.exists(p)
    
    if hasattr(cleanup_temp, 'cleanup_files'):
        cleanup_temp.cleanup_files(str(tmp_path))
        assert not os.path.exists(p)