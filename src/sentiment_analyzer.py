"""
Sentiment analysis utilities.

This module contains functions for performing sentiment analysis
on customer reviews using VADER and other techniques.
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Dict, List


class SentimentAnalyzer:
    """
    Sentiment analyzer using VADER.
    """

    def __init__(self):
        """Initialize the VADER sentiment analyzer."""
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment of a single text.

        Args:
            text: Review text to analyze

        Returns:
            Dictionary with sentiment scores (neg, neu, pos, compound)
        """
        return self.analyzer.polarity_scores(text)

    def classify_sentiment(self, compound_score: float) -> str:
        """
        Classify sentiment based on compound score.

        Args:
            compound_score: VADER compound score (-1 to 1)

        Returns:
            Sentiment label: 'positive', 'negative', or 'neutral'
        """
        if compound_score >= 0.05:
            return "positive"
        elif compound_score <= -0.05:
            return "negative"
        else:
            return "neutral"

    def analyze_dataframe(
        self, df: pd.DataFrame, text_column: str = "review_text"
    ) -> pd.DataFrame:
        """
        Analyze sentiment for entire dataframe.

        Args:
            df: DataFrame with review text
            text_column: Name of column containing text

        Returns:
            DataFrame with added sentiment columns
        """
        # Get sentiment scores for each review
        sentiments = df[text_column].apply(self.analyze_sentiment)

        # Extract individual scores
        df["sentiment_neg"] = sentiments.apply(lambda x: x["neg"])
        df["sentiment_neu"] = sentiments.apply(lambda x: x["neu"])
        df["sentiment_pos"] = sentiments.apply(lambda x: x["pos"])
        df["sentiment_compound"] = sentiments.apply(lambda x: x["compound"])

        # Classify overall sentiment
        df["sentiment_label"] = df["sentiment_compound"].apply(self.classify_sentiment)

        return df


def get_sentiment_statistics(df: pd.DataFrame) -> Dict:
    """
    Calculate sentiment distribution statistics.

    Args:
        df: DataFrame with sentiment_label column

    Returns:
        Dictionary with sentiment statistics
    """
    stats = {
        "total_reviews": len(df),
        "positive_count": (df["sentiment_label"] == "positive").sum(),
        "negative_count": (df["sentiment_label"] == "negative").sum(),
        "neutral_count": (df["sentiment_label"] == "neutral").sum(),
    }

    # Calculate percentages
    stats["positive_pct"] = (stats["positive_count"] / stats["total_reviews"]) * 100
    stats["negative_pct"] = (stats["negative_count"] / stats["total_reviews"]) * 100
    stats["neutral_pct"] = (stats["neutral_count"] / stats["total_reviews"]) * 100

    return stats


if __name__ == "__main__":
    # Test sentiment analyzer
    analyzer = SentimentAnalyzer()

    test_reviews = [
        "This product is amazing! Best purchase ever!",
        "Terrible quality. Complete waste of money.",
        "It's okay, nothing special.",
    ]

    print("Testing sentiment analysis:\n")
    for review in test_reviews:
        sentiment = analyzer.analyze_sentiment(review)
        label = analyzer.classify_sentiment(sentiment["compound"])
        print(f"Review: {review}")
        print(f"Scores: {sentiment}")
        print(f"Label: {label}\n")
