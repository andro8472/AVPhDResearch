from avphdresearch.ner import extract_entities
from avphdresearch.classification import classify_access, group_by_year, summarise_entities


def test_travel_entities():
    result = extract_entities("Denied access at LHR Terminal 5; the lounge was fully booked.")
    assert result["airport_code"] == ["LHR"]
    assert "Terminal 5" in result["terminal"]
    assert "fully booked" in result["capacity"]


def test_classification():
    result = classify_access("We were denied access to the lounge at LHR Terminal 5.")
    assert result["access_denied"]
    assert "LHR" in result["entities"]["airport_code"]


def test_summary():
    assert summarise_entities([{"entities": {"airport_code": ["LHR"]}}])["airport_code"] == [("LHR", 1)]


def test_group_year():
    grouped, unknown = group_by_year([{"date": "2024-05-02"}, {"date": "invalid"}], "date")
    assert len(grouped[2024]) == 1 and len(unknown) == 1
