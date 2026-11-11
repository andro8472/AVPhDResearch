"""Corpus preparation demonstrations without local paths or external datasets."""

import random
import re


def normalise_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_lines(lines: list[str], parts: int) -> list[list[str]]:
    """Partition lines into ordered, near-equal chunks."""
    if parts < 1:
        raise ValueError("parts must be positive")
    size, extra = divmod(len(lines), parts)
    result = []
    offset = 0
    for i in range(parts):
        end = offset + size + (i < extra)
        result.append(lines[offset:end])
        offset = end
    return result


def sample_lines(lines: list[str], count: int, seed: int = 42) -> list[str]:
    """Sample without replacement using a reproducible random seed."""
    if count < 0:
        raise ValueError("count must not be negative")
    return random.Random(seed).sample(lines, min(count, len(lines)))
