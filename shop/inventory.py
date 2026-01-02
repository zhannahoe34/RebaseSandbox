"""Stock bookkeeping."""

MAX_RESTOCK = 1000


def restock(stock: dict[str, int], item: str, qty: int) -> dict[str, int]:
    """Add qty units of item to stock."""
    if qty <= 0:
        raise ValueError("qty must be positive")
    if qty > MAX_RESTOCK:
        raise ValueError(f"qty must be at most {MAX_RESTOCK}")
    if not item:
        raise ValueError("item name required")
    stock[item] = stock.get(item, 0) + qty
    return stock


def reserve(stock: dict[str, int], item: str, qty: int) -> dict[str, int]:
    """Remove qty units of item from stock for an order."""
    available = stock.get(item, 0)
    taken = min(qty, available)
    stock[item] = available - taken
    return stock


def low_stock(stock: dict[str, int], threshold: int) -> list[str]:
    """Items with at most threshold units, sorted by name."""
    return sorted(item for item, qty in stock.items() if qty <= threshold)
