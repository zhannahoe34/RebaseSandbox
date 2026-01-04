from shop.tax import tax_for


def test_uk_rate():
    assert tax_for("UK") == 0.2
