"""Period aggregation adapted from 5 Visualisations/Charts with periodic.py.

This module separates date bucketing from Excel charts and Tkinter.
"""
from datetime import date, datetime


def period_label(value: date | datetime, choice: int) -> str:
    """Return sortable weekly/monthly/quarterly/half-year/year labels."""
    if not isinstance(value, (date, datetime)):
        raise TypeError("value must be a date or datetime")
    if choice == 1:
        year, week, _ = value.isocalendar()
        return f"{year}-W{week:02d}"
    if choice == 2:
        return f"{value.year}-{value.month:02d}"
    if choice == 3:
        return f"{value.year}Q{(value.month - 1) // 3 + 1}"
    if choice == 4:
        return f"{value.year}-H{(value.month - 1) // 6 + 1}"
    if choice == 5:
        return str(value.year)
    raise ValueError("choice must be 1 (week) through 5 (year)")


def aggregate_counts(dates: list[date | datetime], choice: int) -> dict[str, int]:
    from collections import Counter

    counts = Counter(period_label(d, choice) for d in dates)
    return dict(sorted(counts.items()))
