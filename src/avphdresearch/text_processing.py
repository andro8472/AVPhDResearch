"""Non-interactive ports of historical corpus and frequency-table operations.

Sources: Remove_Punct 0.02.py and word frequ table 0.07 -selectable freq.py.
Original Tkinter prompts and local file paths are intentionally omitted.
"""
from collections import Counter
import re
import string

from .ngrams import tokenize

CUSTOM_PUNCTUATION = "…“”’—–"
REMOVE_PUNCTUATION = str.maketrans("", "", string.punctuation + CUSTOM_PUNCTUATION)


def remove_punctuation_and_quotes(text: str) -> str:
    """Remove ASCII punctuation and the source script's typographic marks."""
    return text.translate(REMOVE_PUNCTUATION)


def word_frequency_table(
    text: str,
    stopwords: set[str] | None = None,
    min_frequency: int = 1,
    max_frequency: int | None = None,
    top: int | None = None,
) -> list[tuple[str, int]]:
    """Count words with the historical configurable frequency-range idea."""
    if min_frequency < 1 or (max_frequency is not None and max_frequency < min_frequency):
        raise ValueError("invalid frequency range")
    if top is not None and top < 0:
        raise ValueError("top must be non-negative")
    words = tokenize(text)
    counts = Counter(w for w in words if w not in (stopwords or set()))
    results = [
        (word, frequency)
        for word, frequency in counts.most_common()
        if frequency >= min_frequency
        and (max_frequency is None or frequency <= max_frequency)
    ]
    return results[:top] if top is not None else results
