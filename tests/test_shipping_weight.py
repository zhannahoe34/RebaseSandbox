import pytest

from shop.shipping import shipping_cost


def test_shipping_rejects_non_positive_weight():
    with pytest.raises(ValueError):
        shipping_cost(0)
