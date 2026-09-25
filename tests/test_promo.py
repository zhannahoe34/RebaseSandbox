from shop.promo import promo_price


def test_promo_price():
    assert promo_price(50.0) == 45.0
