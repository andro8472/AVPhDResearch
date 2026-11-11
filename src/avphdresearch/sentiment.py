"""Port of the experimental sentiment classifier from the supplied archive.

Source: Dev/4.2 Sentiment classifier/Sentiment Classifier experimental 0.01.py
The original lexicon import is replaced with explicitly supplied lexicons.
"""
import re

NEGATIONS = {"not", "no", "never", "hardly", "barely"}
INTENSIFIERS = {"very", "extremely", "really", "too", "so"}


def tokenize(text: str) -> list[str]:
    return re.findall(r"\b[\wñáéíóúü]+\b", text.lower())


def score_text(
    text: str, negative_keywords: set[str], positive_keywords: set[str]
) -> tuple[int, list[str]]:
    words = tokenize(text)
    score = 0
    details: list[str] = []
    for i, word in enumerate(words):
        prev = words[i - 1] if i > 0 else None
        prev2 = words[i - 2] if i > 1 else None
        if word in negative_keywords:
            weight = -2
            if prev in INTENSIFIERS:
                weight -= 1
            category = "NEG"
        elif word in positive_keywords:
            weight = 2
            if prev in INTENSIFIERS:
                weight += 1
            category = "POS"
        else:
            continue
        if prev in NEGATIONS or prev2 in NEGATIONS:
            weight = -weight
        score += weight
        details.append(f"{category}({word}:{weight})")
    return score, details


def classify_sentiment(
    text: str, negative_keywords: set[str], positive_keywords: set[str]
) -> tuple[str, int, list[str]]:
    if not isinstance(text, str) or not text.strip():
        return "neutral", 0, []
    score, details = score_text(text, negative_keywords, positive_keywords)
    if score <= -2:
        return "negative", score, details
    if score >= 2:
        return "positive", score, details
    return "neutral", score, details
