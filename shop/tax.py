"""Sales tax by region."""


def tax_for(region: str) -> float:
    """Tax rate for a region; unknown regions are untaxed."""
    rates = {
        "US": 0.07,
        "EU": 0.2,
        "UK": 0.2,
        "CA": 0.05,
    }
    return rates.get(region, 0.0)
