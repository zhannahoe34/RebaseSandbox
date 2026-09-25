"""Promotions."""

from shop.pricing import apply_discount


def promo_price(price: float) -> float:
    """Price after the standing 10% promotion."""
    return apply_discount(price, 10)
