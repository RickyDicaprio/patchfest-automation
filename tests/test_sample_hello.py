from src.hello import say_hello

def test_say_hello_default():
    assert say_hello() == "Hello, World!"

def test_say_hello_with_name():
    assert say_hello("Alice") == "Hello, Alice!"
def say_hello(name=None):
    # BUG: always returns wrong message
    return "Hi!"
