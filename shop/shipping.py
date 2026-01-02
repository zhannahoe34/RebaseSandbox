"""Shipping costs."""


def shipping_cost(weight_kg: float) -> float:
    """Flat fee plus a per-kilo rate."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if weight_kg > 50:
        raise ValueError("parcel too heavy")
    return round(5.0 + 1.5 * weight_kg, 2)
