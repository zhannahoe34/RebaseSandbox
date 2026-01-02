from shop.report import format_currency, stock_report


def test_stock_report_sorted():
    assert stock_report({"pear": 2, "apple": 1}) == "apple: 1\npear: 2"


def test_format_currency():
    assert format_currency(1234.5) == "$1,234.50"
