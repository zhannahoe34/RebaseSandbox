from shop.cart import cart_total


def test_cart_total():
    assert cart_total([(2.5, 4), (1.0, 3)]) == 13.0
