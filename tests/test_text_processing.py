from avphdresearch.text_processing import remove_punctuation_and_quotes, word_frequency_table


def test_punctuation():
    assert remove_punctuation_and_quotes("Hello, ‘world’—yes!") == "Hello ‘worldyes"


def test_frequencies():
    assert word_frequency_table("cat dog cat bird", min_frequency=2) == [("cat", 2)]


def test_stopwords():
    assert word_frequency_table("the cat the", stopwords={"the"}) == [("cat", 1)]
