import pytest

from shop.inventory import restock


def test_restock_rejects_empty_item():
    with pytest.raises(ValueError):
        restock({}, "", 1)
