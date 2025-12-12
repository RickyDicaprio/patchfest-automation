from src.utils import (
    add_numbers,
    reverse_string,
    count_words
)

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_reverse_string():
    assert reverse_string("abc") == "cba"

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("") == 0

def add_numbers(a, b):
    # BUG: wrong math
    return a - b

def reverse_string(s):
    # BUG: returns same string
    return s

def count_words(text):
    # BUG: counts characters not words
    return len(text)
