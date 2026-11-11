import pytest

from avphdresearch.ngrams import ngram_frequencies


def test_repeated_bigram():
    assert ngram_frequencies("red blue red blue")[("red", "blue")] == 2


def test_invalid_n():
    with pytest.raises(ValueError):
        ngram_frequencies("hello", 0)
