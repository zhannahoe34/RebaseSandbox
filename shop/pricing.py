"""Price calculations."""


def calc_price(base: float, qty: int, tax_rate: float) -> float:
    """Tax-inclusive total for qty units at the given base price."""
    if qty < 0:
        raise ValueError("qty must be non-negative")
    return round(base * qty * (1 + tax_rate), 2)


def apply_discount(price: float, pct: float) -> float:
    """Apply a discount given as a fraction (0-1)."""
    if not 0 <= pct <= 1:
        raise ValueError("pct must be between 0 and 1")
    return round(price * (1 - pct), 2)
