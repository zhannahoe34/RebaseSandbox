from shop.report import stock_report, total_units


def test_stock_report_sorted():
    assert stock_report({"pear": 2, "apple": 1}) == "apple: 1\npear: 2"


def test_total_units():
    assert total_units({"apple": 1, "pear": 2}) == 3
