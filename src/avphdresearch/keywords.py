"""Simple case-insensitive, whole-word keyword matching."""

import re


def matched_keywords(text: str, keywords: set[str]) -> list[str]:
    return sorted(
        keyword
        for keyword in keywords
        if re.search(r"\b" + re.escape(keyword) + r"\b", text, re.IGNORECASE)
    )
