"""Source-derived access classification with nearby travel entities.

Based on the main Keyword Classifier- Turn away-NER 0.12.5.py's
detect_access / find_entities / context-window workflow.
"""
from collections import Counter
from datetime import datetime
from typing import Any

from .ner import extract_entities
from .turnaway import matches_turnaway


def classify_access(text: str, context_window: int = 200) -> dict[str, Any]:
    """Classify a review and extract entities from the review context."""
    if context_window < 0:
        raise ValueError("context_window must be non-negative")
    if not isinstance(text, str):
        text = ""
    matched = matches_turnaway(text)
    return {
        "access_denied": matched,
        "category": "Turned away / denied entry" if matched else "no_match",
        "entities": extract_entities(text) if matched else {},
    }


def summarise_entities(results: list[dict], category: str | None = None, min_count: int = 1) -> dict[str, list[tuple[str, int]]]:
    """Count detected entities across classified reviews."""
    if min_count < 1:
        raise ValueError("min_count must be positive")
    counts: dict[str, Counter] = {}
    for row in results:
        for cat, values in row.get("entities", {}).items():
            if category is None or cat == category:
                counts.setdefault(cat, Counter()).update(values)
    return {cat: [(name, count) for name, count in counter.most_common() if count >= min_count] for cat, counter in counts.items()}


def group_by_year(rows: list[dict], date_field: str) -> tuple[dict[int, list[dict]], list[dict]]:
    """Group classified rows by ISO-format dates, retaining invalid dates separately."""
    years: dict[int, list[dict]] = {}
    unknown: list[dict] = []
    for row in rows:
        raw = str(row.get(date_field, "")).strip()
        try:
            year = datetime.fromisoformat(raw.replace("Z", "+00:00")).year
        except ValueError:
            unknown.append(row)
        else:
            years.setdefault(year, []).append(row)
    return dict(sorted(years.items())), unknown
