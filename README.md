# AVPhDResearch — NLP and Text Mining Research

**Andrew Vassiliou, PhD** · University of Surrey

A curated portfolio of Python research workflows for text mining, corpus analysis, information extraction and NLP. The original PhD, *Analysing Film Content: a Text-based Approach*, explored extracting events and narrative information from film scripts and audio-description text.

## Portfolio contents

| Area | Included |
| --- | --- |
| Corpus preparation | Punctuation removal, balanced corpus splitting, repeatable sampling and configurable word-frequency filtering |
| Corpus analysis | N-grams, collocations, stopword filtering and a runnable example using a synthetic corpus |
| Sentiment and language | Experimental rule-based sentiment scoring, VADER score thresholds and optional language detection |
| Classification and entity extraction | Rule-based lounge access-denial classification, travel entity matching with a curated lexicon, and summaries grouped by year |
| Reporting | Weekly through yearly date bucketing |
| Documentation and testing | Research context, a map from original scripts to current modules, synthetic test fixtures and automated Python tests through GitHub Actions |

The public portfolio excludes the original film scripts, audio descriptions and OpenAI key test. The original Excel dashboards and desktop interfaces remain outside the migrated scope. The published modules have yet to be benchmarked against the original thesis datasets. See the [migration status](docs/migration-status.md) for script-level coverage.

## Research areas

| Stage | Focus | Source archive |
|---|---|---|
| 01 | Text ingestion and corpus preparation | `0 Raw Text`, `1 Raw Text`, `2 Corpora & Text Prep` |
| 02 | Language detection, stoplists and frequencies | `3 Text Processing` |
| 03 | N-grams, collocations and lexical patterns | `4.1 Colocation` |
| 04 | Rule-based sentiment exploration | `4.2 Sentiment classifier` |
| 05 | Keyword classification, regex and named entities | `4.3 Keyword Classification Explorer` |
| 06 | Reporting, time series and visualisation | `5 Visualisations` |

## Start here

This branch is a **portfolio structure and safe demonstration**, not a claim that all historical scripts are runnable or experimentally validated.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
python -m pip install -e ".[dev]"
python -m pytest
python -m avphdresearch.ngrams examples/sample_corpus.txt --n 2
```

## Contents

- `src/avphdresearch/` — small, importable NLP demonstration utilities
- `tests/` — automated tests using original synthetic fixtures
- `examples/` — synthetic demonstration corpus
- `docs/` — research overview, provenance and migration plan
- `data/README.md` — instructions for licensed local datasets
- `archive/README.md` — how experimental versions are retained outside the public repo

## Publication safeguards

The supplied development archive includes third-party film scripts, research corpora, many numbered experimental versions and a file named `OpenAI key test.py`. **None of those original files are included in this public portfolio branch.** The original archive should remain backed up privately. Review licences and credentials before importing additional files.

## Research provenance

See [research context](docs/research-context.md) and [migration map](docs/migration-map.md). This demonstration has not been benchmarked against the thesis datasets.

## Rights

Copyright Andrew Vassiliou. All rights reserved pending a deliberate licence decision.
