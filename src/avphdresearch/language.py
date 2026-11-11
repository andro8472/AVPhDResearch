"""Language detection core adapted from foreign_language_detect_excel.py.

Optional langdetect backend. No silent heuristic claiming reliable language ID.
"""
import re


def enough_signal(text: str, min_chars: int = 30, min_alpha: int = 15) -> bool:
    if len(text) < min_chars:
        return False
    return len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]", text)) >= min_alpha


def detect_language(text: str) -> tuple[str, float, str]:
    """Return language, estimated confidence and backend; unknown if unavailable."""
    if not isinstance(text, str) or not enough_signal(text):
        return "unknown", 0.0, "insufficient_text"
    try:
        from langdetect import DetectorFactory, detect_langs
    except ImportError:
        return "unknown", 0.0, "not_installed"
    DetectorFactory.seed = 0
    try:
        candidates = detect_langs(text)
    except Exception:
        return "unknown", 0.0, "langdetect_error"
    if not candidates:
        return "unknown", 0.0, "langdetect"
    return candidates[0].lang, float(candidates[0].prob), "langdetect"
