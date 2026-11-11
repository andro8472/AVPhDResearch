# Source archive migration map

This branch establishes a clean public structure. It does **not** upload the complete original ZIP.

| Original development folders | Proposed location | Status |
| --- | --- | --- |
| `0 Raw Text`, `1 Raw Text` | `src/avphdresearch/ingestion/` | Review PDF/OCR/audio dependencies and source rights |
| `2 Corpora & Text Prep` | `src/avphdresearch/corpus.py` | Minimal illustrative utilities |
| `3 Text Processing` | `src/avphdresearch/text_processing/` | Review stoplists, language detection, frequency scripts |
| `4.1 Colocation` | `src/avphdresearch/ngrams.py` | Minimal illustrative n-gram utility |
| `4.2 Sentiment classifier` | `src/avphdresearch/sentiment/` | Historical algorithm not yet migrated |
| `4.3 Keyword Classification Explorer` | `src/avphdresearch/keywords.py` and `ner/` | Generic keyword demo; historical classifier not yet migrated |
| `5 Visualisations` | `src/avphdresearch/visualisation/` | Not migrated; dependent on Excel/research datasets |
| `Older/` and numbered versions | Private historical archive | Keep source ZIP backed up, review selectively |

## Safeguards

- Exclude `OpenAI key test.py` and any credentials.
- Do not publish third-party film scripts, audio descriptions, bulk corpora or unlicensed data.
- Check historical scripts for absolute Windows paths, hidden assumptions, GUI dependencies and imports.
- Add approved, anonymised fixtures and documented evaluation before claiming reproducibility.
