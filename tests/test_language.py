from avphdresearch.language import detect_language, enough_signal


def test_short_text():
    assert not enough_signal("hi")
    assert detect_language("hi") == ("unknown", 0.0, "insufficient_text")
