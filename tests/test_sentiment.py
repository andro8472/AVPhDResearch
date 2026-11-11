from avphdresearch.sentiment import classify_sentiment


def test_positive_intensifier():
    assert classify_sentiment("very good", {"bad"}, {"good"})[:2] == ("positive", 3)


def test_negation():
    assert classify_sentiment("not good", {"bad"}, {"good"})[:2] == ("negative", -2)


def test_negative():
    assert classify_sentiment("really bad", {"bad"}, {"good"})[:2] == ("negative", -3)


def test_empty():
    assert classify_sentiment("", {"bad"}, {"good"}) == ("neutral", 0, [])
