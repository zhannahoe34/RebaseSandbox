from shop.greeting import greet


def test_greet():
    assert greet("Ann") == "Hello, Ann!"
