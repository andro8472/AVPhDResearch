# Migration progress

## Source-based ports in this commit

The following modules are based on specific original scripts in the uploaded `Dev.zip`, not invented replacements:

1. `sentiment.py` — `4.2 Sentiment classifier/Sentiment Classifier experimental 0.01.py`: keyword lexicons, ±2 weighting, intensifiers, local negation and thresholds. The historical import of `negative_keywords` is replaced by explicit lexicon parameters.
2. `turnaway.py` — `4.3 Keyword Classification Explorer/TurnawayKwdsRgx.py`: the source's lounge-access denial patterns and pre-cleaning expressions.
3. `text_processing.py` — `2 Corpora & Text Prep/Remove_Punct 0.02.py` and `3 Text Processing/word frequ table 0.07 -selectable freq.py`: punctuation handling and configurable frequency filtering; file dialogs and GUI have been replaced with callable functions.

These are **adapted ports**, not byte-for-byte copies. Tests cover selected synthetic cases only. There is no assertion that they reproduce published thesis results.

## Still to migrate

- Full `Keyword Classifier- Turn away-NER 0.12.5.py` and `ner_lists3.py` (larger domain-specific model and external entity lists)
- Streaming NLTK collocations and stoplist handling
- Corpus splitting and sentiment partitioning
- Foreign-language detection
- Visualisation and dashboard scripts

## Security and data

`OpenAI key test.py` is excluded. No original film scripts or bulk data are published. The historical scripts should be reviewed for credentials, copyright, local paths and external dependencies before any direct publication.
