"""VADER sentiment bucket helper from sentiment split 0.01.py.

Requires the optional NLTK package and its VADER lexicon data.
"""


def classify_vader(text: str, analyser) -> str:
    """Use source thresholds: positive >= 0.05, negative <= -0.05."""
    if not isinstance(text, str):
        return "neutral"
    compound = analyser.polarity_scores(text)["compound"]
    return "positive" if compound >= 0.05 else "negative" if compound <= -0.05 else "neutral"


def bucket_sentiments(texts: list[str], analyser) -> dict[str, list[str]]:
    buckets: dict[str, list[str]] = {"positive": [], "negative": [], "neutral": []}
    for text in texts:
        buckets[classify_vader(text, analyser)].append(text)
    return buckets
