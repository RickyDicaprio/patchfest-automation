import sys
from scripts import sample_hello

def test_hello_output(capsys):
    if hasattr(sample_hello, 'main'):
        sample_hello.main()
    
    captured = capsys.readouterr()
    assert len(captured.out) > 0