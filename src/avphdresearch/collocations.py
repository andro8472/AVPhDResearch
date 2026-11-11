"""N-gram analysis adapted from 4.1 Colocation/n-grams 0.04.py.

The historical NLTK/Tkinter UI is replaced by a dependency-free core.
"""
from collections import Counter

from .ngrams import tokenize


def collocations(text: str, n: int = 2, stopwords: set[str] | None = None, top: int | None = 20) -> list[tuple[tuple[str, ...], int]]:
    """Count contiguous word n-grams, optionally removing stopword-containing spans."""
    if n < 1:
        raise ValueError("n must be positive")
    if top is not None and top < 0:
        raise ValueError("top must be non-negative")
    words = tokenize(text)
    excluded = stopwords or set()
    counts = Counter(
        tuple(words[i:i + n])
        for i in range(max(0, len(words) - n + 1))
        if not any(word in excluded for word in words[i:i + n])
    )
    return counts.most_common(top)
