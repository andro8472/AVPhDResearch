from avphdresearch.corpus import normalise_whitespace, sample_lines, split_lines


def test_normalise_whitespace():
    assert normalise_whitespace(" a\n  b\t") == "a b"


def test_split():
    assert split_lines(["a", "b", "c", "d", "e"], 2) == [
        ["a", "b", "c"], ["d", "e"]
    ]


def test_sample_reproducibility():
    lines = list("abcdefgh")
    assert sample_lines(lines, 3, seed=4) == sample_lines(lines, 3, seed=4)
