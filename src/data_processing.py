"""
Data processing utilities for sentiment analysis project.

This module contains functions for loading, cleaning, and preprocessing
customer review data.
"""

import pandas as pd
import re
from typing import Optional


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load raw data from CSV file.

    Args:
        filepath: Path to the CSV file

    Returns:
        DataFrame containing the raw data
    """
    # TODO: Implement data loading
    pass


def clean_text(text: str) -> str:
    """
    Clean and preprocess review text.

    Args:
        text: Raw review text

    Returns:
        Cleaned text string
    """
    if not isinstance(text, str):
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www.\S+", "", text)

    # Remove special characters but keep spaces and basic punctuation
    text = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", text)

    # Remove extra whitespace
    text = " ".join(text.split())

    return text


def preprocess_dataframe(
    df: pd.DataFrame, text_column: str = "review_text"
) -> pd.DataFrame:
    """
    Preprocess the entire dataframe.

    Args:
        df: Raw dataframe
        text_column: Name of the column containing review text

    Returns:
        Preprocessed dataframe
    """
    # TODO: Implement full preprocessing pipeline
    # - Handle missing values
    # - Clean text
    # - Convert dates
    # - Filter invalid entries
    pass


def save_processed_data(df: pd.DataFrame, filepath: str) -> None:
    """
    Save processed data to CSV.

    Args:
        df: Processed dataframe
        filepath: Output file path
    """
    df.to_csv(filepath, index=False)
    print(f"Processed data saved to {filepath}")


if __name__ == "__main__":
    # Test functions here
    sample_text = (
        "This is a GREAT product!!! Check it out at http://example.com #amazing"
    )
    print(f"Original: {sample_text}")
    print(f"Cleaned: {clean_text(sample_text)}")
