from avphdresearch.keywords import matched_keywords


def test_whole_word():
    assert matched_keywords("The cat sat", {"cat", "at"}) == ["cat"]
