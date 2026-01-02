import pytest

from shop.inventory import reserve


def test_reserve_reports_shortfall():
    with pytest.raises(ValueError, match="short by 1"):
        reserve({"apple": 1}, "apple", 2)
