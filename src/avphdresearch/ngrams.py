"""Basic frequency and n-gram demonstration using the standard library."""

import argparse
from collections import Counter
from pathlib import Path
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)?", text.lower())


def ngram_frequencies(text: str, n: int = 2) -> Counter[tuple[str, ...]]:
    if n < 1:
        raise ValueError("n must be positive")
    words = tokenize(text)
    return Counter(tuple(words[i:i + n]) for i in range(len(words) - n + 1))


def main() -> None:
    parser = argparse.ArgumentParser(description="Count n-grams in a UTF-8 text file")
    parser.add_argument("file", type=Path)
    parser.add_argument("--n", type=int, default=2)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()
    for phrase, count in ngram_frequencies(
        args.file.read_text(encoding="utf-8"), args.n
    ).most_common(args.top):
        print(f"{' '.join(phrase)}\t{count}")


if __name__ == "__main__":
    main()
