"""Turn-away / denied-entry rule matching ported from TurnawayKwdsRgx.py.

Source: Dev/4.3 Keyword Classification Explorer/TurnawayKwdsRgx.py.
Patterns are specific to lounge-access complaints and are not a general NER model.
"""
import re

LOUNGE_TURNAWAY_REGEX = {
    "Turned away / denied entry": [
        r"\bturn(?:ed|ing)?(?:\s*[-_]\s*|\s+)(?:us|me|him|her|them|you)?\s*(?:\s*[-_]\s*|\s+)?away\b",
        r"\b(?:was|were|been|has\s+been|have\s+been|is\s+being|are\s+being)\s+turn\s+away\b",
        r"(?:\blounge(?:s)?\b(?:\s+\w+){0,6}\s+turn(?:ed|ing)?\s+away\b|\bturn(?:ed|ing)?\s+away\b(?:\s+\w+){0,6}\s+\blounge(?:s)?\b)",
        r"\baccess\s+denied\b(?:\s+(?:at|to|into|in|from))?(?:\s+(?:the|a))?\s+lounge(?:s)?\b",
        r"\bdenied\b(?:\s+access)?(?:\s+(?:at|to|into|in|from))?(?:\s+(?:the|a))?\s+lounge(?:s)?\b",
        r"\b(?:refused|rejected|declined)\b(?:\s+(?:entry|access))?(?:\s+(?:to|into|in|at|from))?(?:\s+(?:the|a))?\s+lounge(?:s)?\b",
        r"\b(?:can(?:not|'t)|cant|unable\s+to)\s+(?:access|enter|use|book)\b(?:\s+(?:the|a))?\s+lounge(?:s)?\b",
        r"\bnot\s+(?:allowed|accepted)\b(?:\s+(?:in|into|to|at|from))?(?:\s+(?:the|a))?\s+lounge(?:s)?\b",
        r"\blounge(?:s)?\b(?:\s+\w+){0,3}\s+\b(?:denied|refused|rejected|declined)\b",
    ],
    "Pre-clean suggestions": [r"\blin\b", r"x000d"],
}
TURN_AWAY_RX = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in LOUNGE_TURNAWAY_REGEX["Turned away / denied entry"]
]


def normalise_text(text: str) -> str:
    for pattern in LOUNGE_TURNAWAY_REGEX["Pre-clean suggestions"]:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def matches_turnaway(text: str) -> bool:
    cleaned = normalise_text(text)
    return any(regex.search(cleaned) for regex in TURN_AWAY_RX)
