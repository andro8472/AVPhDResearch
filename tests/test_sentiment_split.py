from avphdresearch.sentiment_split import bucket_sentiments, classify_vader


class FakeAnalyser:
    def polarity_scores(self, text):
        return {"compound": {"good": 0.6, "bad": -0.5}.get(text, 0.0)}


def test_buckets():
    assert bucket_sentiments(["good", "bad", "okay"], FakeAnalyser()) == {
        "positive": ["good"], "negative": ["bad"], "neutral": ["okay"]
    }
