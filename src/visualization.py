"""
Visualization utilities for sentiment analysis results.

This module contains functions for creating charts and plots
to visualize sentiment patterns and insights.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional

# Set style for all plots
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


def plot_sentiment_distribution(
    df: pd.DataFrame, save_path: Optional[str] = None
) -> None:
    """
    Create bar chart showing distribution of sentiment labels.

    Args:
        df: DataFrame with sentiment_label column
        save_path: Optional path to save the figure
    """
    plt.figure(figsize=(10, 6))

    sentiment_counts = df["sentiment_label"].value_counts()
    colors = {"positive": "#2ecc71", "neutral": "#95a5a6", "negative": "#e74c3c"}

    bars = plt.bar(
        sentiment_counts.index,
        sentiment_counts.values,
        color=[colors.get(x, "#3498db") for x in sentiment_counts.index],
    )

    plt.title(
        "Sentiment Distribution of Customer Reviews", fontsize=16, fontweight="bold"
    )
    plt.xlabel("Sentiment", fontsize=12)
    plt.ylabel("Number of Reviews", fontsize=12)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=11,
        )

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Figure saved to {save_path}")

    plt.show()


def plot_sentiment_over_time(
    df: pd.DataFrame, date_column: str = "date", save_path: Optional[str] = None
) -> None:
    """
    Create line chart showing sentiment trends over time.

    Args:
        df: DataFrame with sentiment scores and date column
        date_column: Name of the date column
        save_path: Optional path to save the figure
    """
    # TODO: Implement time series visualization
    pass


def plot_compound_score_distribution(
    df: pd.DataFrame, save_path: Optional[str] = None
) -> None:
    """
    Create histogram of compound sentiment scores.

    Args:
        df: DataFrame with sentiment_compound column
        save_path: Optional path to save the figure
    """
    plt.figure(figsize=(10, 6))

    plt.hist(
        df["sentiment_compound"], bins=50, color="#3498db", alpha=0.7, edgecolor="black"
    )
    plt.axvline(x=0.05, color="green", linestyle="--", label="Positive threshold")
    plt.axvline(x=-0.05, color="red", linestyle="--", label="Negative threshold")

    plt.title(
        "Distribution of Sentiment Compound Scores", fontsize=16, fontweight="bold"
    )
    plt.xlabel("Compound Score", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.legend()

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Figure saved to {save_path}")

    plt.show()


def plot_sentiment_by_category(
    df: pd.DataFrame, category_column: str = "category", save_path: Optional[str] = None
) -> None:
    """
    Create grouped bar chart showing sentiment distribution by category.

    Args:
        df: DataFrame with sentiment_label and category columns
        category_column: Name of the category column
        save_path: Optional path to save the figure
    """
    # TODO: Implement category comparison visualization
    pass


def create_wordcloud(
    df: pd.DataFrame,
    sentiment: str = "positive",
    text_column: str = "review_text",
    save_path: Optional[str] = None,
) -> None:
    """
    Create word cloud for reviews of specific sentiment.

    Args:
        df: DataFrame with review text and sentiment labels
        sentiment: 'positive', 'negative', or 'neutral'
        text_column: Name of column containing review text
        save_path: Optional path to save the figure
    """
    # TODO: Implement word cloud generation
    pass


if __name__ == "__main__":
    # Test visualization with sample data
    sample_data = pd.DataFrame(
        {
            "sentiment_label": ["positive"] * 150
            + ["negative"] * 50
            + ["neutral"] * 30,
            "sentiment_compound": [0.5] * 150 + [-0.5] * 50 + [0.0] * 30,
        }
    )

    print("Creating sample visualizations...")
    plot_sentiment_distribution(sample_data)
    plot_compound_score_distribution(sample_data)
