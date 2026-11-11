# Source archive migration status

This repository selectively ports the most reusable algorithms from the user's `Dev.zip`. The source ZIP is retained separately; this public repository is not a complete archive.

| Original file | Module | Coverage |
| --- | --- | --- |
| `Corpus split 0.01.py` | `corpus.py` | Balanced partitioning and seeded sampling; GUI removed |
| `word frequ table 0.07 -selectable freq.py` | `text_processing.py` | Configurable frequency filtering |
| `Remove_Punct 0.02.py` | `text_processing.py` | Punctuation removal |
| `n-grams 0.04.py` | `collocations.py` | Contiguous n-grams and stopword filtering; NLTK UI not reproduced |
| `Sentiment Classifier experimental 0.01.py` | `sentiment.py` | Experimental rule scoring |
| `sentiment split 0.01.py` | `sentiment_split.py` | VADER thresholds and bucket splitting; Excel IO omitted |
| `foreign_language_detect_excel.py` | `language.py` | Signal check and optional langdetect backend; GUI/Excel omitted |
| `TurnawayKwdsRgx.py` | `turnaway.py` | Lounge-access denial patterns |
| `Keyword Classifier- Turn away-NER 0.12.5.py` | `classification.py` | Access classification, entity summaries, year grouping; adapted subset |
| `ner_lists3.py` | `ner.py` | **Curated subset** of travel lexicons and canonical terminal matching |
| `Charts with periodic.py` | `periods.py` | Weekly to yearly date bucketing; Excel chart rendering omitted |
| `TP Dashboards Hot spot.py` | Not yet ported | Excel dashboards/hotspot matrix not reproduced |

## Deliberate exclusions

- `OpenAI key test.py`, potential credentials and external API examples.
- Film scripts, audio descriptions, raw corpora and other unverified third-party datasets.
- Old numbered experimental versions and redundant GUI variants.
- Large, unreviewed dictionaries, spreadsheets and executable desktop front ends.

## Scientific limitations

These modules are adapted from research and later experimental scripts, not guaranteed thesis reproductions. Tests use synthetic fixtures; no original corpus benchmarks or academic metrics are asserted. The regex NER is a **rule-based entity matcher**, not a trained statistical model. Source dictionaries were intentionally reduced and require further review for production use.

## Suggested follow-up

For a more complete research demonstration, add licensed/anonymised evaluation datasets, document precision/recall, and migrate the dashboard with validated sample data.
