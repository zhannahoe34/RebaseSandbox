import pytest

from shop.shipping import shipping_cost


def test_shipping_rejects_heavy_parcels():
    with pytest.raises(ValueError):
        shipping_cost(51)
