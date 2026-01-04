import pytest
from shop.inventory import low_stock, reserve, restock


def test_restock_adds():
    assert restock({"apple": 1}, "apple", 2) == {"apple": 3}


def test_restock_rejects_non_positive():
    with pytest.raises(ValueError):
        restock({}, "apple", 0)


def test_reserve_removes():
    assert reserve({"apple": 3}, "apple", 2) == {"apple": 1}


def test_reserve_takes_what_is_left():
    assert reserve({"apple": 1}, "apple", 2) == {"apple": 0}


def test_low_stock():
    assert low_stock({"apple": 1, "pear": 5, "fig": 0}, 1) == ["apple", "fig"]


def test_restock_rejects_over_max():
    with pytest.raises(ValueError):
        restock({}, "apple", 1001)
