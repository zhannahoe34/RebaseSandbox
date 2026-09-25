from shop.auth.tokens import expired


def test_expired():
    assert not expired(0.0, 10.0)
    assert expired(0.0, 4000.0)
