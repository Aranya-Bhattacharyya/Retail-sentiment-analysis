from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_sentiment_score(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)
