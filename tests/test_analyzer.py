from src.analyzer import get_sentiment_score

def test_positive_logic():
    result = get_sentiment_score("I love this product!")
    assert result['compound'] > 0

def test_negative_logic():
    result = get_sentiment_score("This is terrible.")
    assert result['compound'] < 0