from shop.tax import tax_for


def test_canada_rate():
    assert tax_for("CA") == 0.05
