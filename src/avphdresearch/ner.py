"""Domain-specific, rule-based travel entity extraction.

Adapted from ner_lists3.py and Keyword Classifier- Turn away-NER 0.12.5.py.
This is a curated subset of the historical dictionaries, not a trained NER model.
"""
import re

TERMINAL_CANON = {
    "Terminal 1": r"\b(?:terminal\s*1|terminal1|t\s*1|term\s*1|terminal one)\b",
    "Terminal 2": r"\b(?:terminal\s*2|terminal2|t\s*2|term\s*2|terminal two)\b",
    "Terminal 3": r"\b(?:terminal\s*3|terminal3|t\s*3|term\s*3|terminal three)\b",
    "Terminal 4": r"\b(?:terminal\s*4|terminal4|t\s*4|term\s*4|terminal four)\b",
    "Terminal 5": r"\b(?:terminal\s*5|terminal5|t\s*5|term\s*5|terminal five)\b",
    "North Terminal": r"\bnorth\s+terminal\b",
    "South Terminal": r"\bsouth\s+terminal\b",
}
AIRPORT_CODES = frozenset({"LHR", "LGW", "STN", "LTN", "MAN", "JFK", "LAX", "AMS", "CDG", "DXB", "PFO", "LCA"})
AIRPORT_NAMES = frozenset({"heathrow", "gatwick", "stansted", "luton", "manchester", "schiphol", "changi"})
CAPACITY_PHRASES = frozenset({"no space", "limited space", "space constraints", "crowded", "fully booked", "no room", "lounge is busy"})
PP_ACCESS_RESTRICTED = frozenset({"not accepting pp", "restricted access pp", "closed for pp", "don't accept pp"})
LOUNGE_CODE_RX = re.compile(r"(?<![A-Z0-9])(?P<iata>[A-Z]{3})(?P<num>\d{1,2})(?![A-Z0-9])")
AIRPORT_CODE_RX = re.compile(r"(?<![A-Z0-9])(?P<iata>[A-Z]{3})(?=(?:[^A-Z0-9]|$)|\d{1,2}(?!\d))")


def _phrases(text: str, phrases: frozenset[str]) -> list[str]:
    return sorted(p for p in phrases if re.search(r"(?<!\w)" + re.escape(p) + r"(?!\w)", text, re.I))


def extract_entities(text: str) -> dict[str, list[str]]:
    """Extract a compact, auditable subset of the source's travel entities."""
    if not isinstance(text, str):
        return {}
    entities: dict[str, list[str]] = {}
    for canon, pattern in TERMINAL_CANON.items():
        matches = re.findall(pattern, text, flags=re.I)
        if matches:
            entities.setdefault("terminal", []).extend([canon] * len(matches))
    codes = [
        m.group("iata") + m.group("num")
        for m in LOUNGE_CODE_RX.finditer(text.upper())
        if m.group("iata") in AIRPORT_CODES
    ]
    if codes:
        entities["loungecode"] = codes
    airports = [m.group("iata") for m in AIRPORT_CODE_RX.finditer(text) if m.group("iata") in AIRPORT_CODES]
    if airports:
        entities["airport_code"] = airports
    for category, terms in (
        ("airport_name", AIRPORT_NAMES),
        ("capacity", CAPACITY_PHRASES),
        ("pp_access", PP_ACCESS_RESTRICTED),
    ):
        found = _phrases(text, terms)
        if found:
            entities[category] = found
    return entities
