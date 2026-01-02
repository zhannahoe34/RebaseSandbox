"""Shopping cart totals."""

from shop.pricing import calc_price


def cart_total(items: list[tuple[float, int]]) -> float:
    """Sum of line prices for (unit_price, qty) pairs."""
    return round(sum(calc_price(price, qty) for price, qty in items), 2)
