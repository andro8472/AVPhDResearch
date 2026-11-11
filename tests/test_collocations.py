from avphdresearch.collocations import collocations


def test_bigram():
    assert collocations("red blue red blue", 2)[0] == (("red", "blue"), 2)


def test_stopwords():
    assert collocations("the blue lounge", 2, {"the"}) == [(("blue", "lounge"), 1)]
