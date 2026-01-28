# Retail Customer Sentiment Analysis

An NLP pipeline for analyzing customer reviews to extract actionable business insights and sentiment patterns.

## Project Overview

This project analyzes customer reviews from retail products to understand sentiment trends, identify common complaints and praise points, and provide data-driven recommendations for business improvement.

**Status**: In Development

## Business Problem

Retail companies receive thousands of customer reviews across multiple products. Manually analyzing this feedback is time-consuming and prone to missing important patterns. This project automates sentiment analysis to help businesses:

- Identify products with negative sentiment trends
- Understand common customer pain points
- Track sentiment changes over time
- Prioritize areas for product improvement

## Dataset

**Source**: [To be determined - options include Amazon Product Reviews, Kaggle retail datasets, or scraped data]

**Size**: Approximately 10,000+ reviews

**Features**:
- Review text
- Product category
- Rating (1-5 stars)
- Review date

## Technical Approach

### Data Processing
1. Text cleaning and preprocessing
2. Tokenization and stopword removal
3. Handling of negations and intensifiers

### Sentiment Analysis
- **Method**: VADER (Valence Aware Dictionary and Sentiment Reasoner) and/or TextBlob
- **Alternative approach**: Fine-tuned transformer model if computational resources allow
- Classification into positive, negative, and neutral sentiment

### Analysis & Insights
- Sentiment distribution by product category
- Temporal sentiment trends
- Word frequency analysis for positive vs negative reviews
- Common themes extraction using topic modeling (optional)

### Visualization
- Sentiment distribution charts
- Word clouds for positive/negative reviews
- Time series sentiment trends
- Category-level sentiment comparison

## Tech Stack

**Languages & Libraries**:
- Python 3.x
- pandas - Data manipulation
- NLTK / spaCy - Text processing
- scikit-learn - Machine learning utilities
- Matplotlib / Seaborn - Visualization
- VADER Sentiment - Sentiment analysis

**Development Environment**:
- Jupyter Notebook for exploration
- Python scripts for production code

## Project Structure

```
retail-sentiment-analysis/
│
├── data/
│   ├── raw/                 # Original dataset
│   └── processed/           # Cleaned data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_sentiment_analysis.ipynb
│
├── src/
│   ├── data_processing.py   # Data cleaning functions
│   ├── sentiment_analyzer.py # Sentiment analysis logic
│   └── visualization.py     # Plotting functions
│
├── results/
│   ├── figures/             # Generated plots
│   └── reports/             # Analysis summaries
│
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Installation & Usage

### Prerequisites
```bash
Python 3.8+
pip
```

### Setup
```bash
# Clone the repository
git clone https://github.com/Aranya-Bhattacharyya/retail-sentiment-analysis.git

# Navigate to project directory
cd retail-sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (if using NLTK)
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('stopwords')"
```

### Running the Analysis
```bash
# Instructions will be added as development progresses
```

## Key Findings

*This section will be populated with insights once analysis is complete.*

## Skills Demonstrated

- Data cleaning and preprocessing
- Natural Language Processing (NLP)
- Sentiment analysis techniques
- Data visualization
- Python programming
- Business insight generation from data

## Future Enhancements

- Implement aspect-based sentiment analysis (analyzing sentiment for specific product features)
- Build a web dashboard for interactive exploration
- Add comparative analysis across different retail categories
- Deploy as a REST API for real-time sentiment scoring

## License

This project is open source and available for educational purposes.

## Contact

Aranya Bhattacharyya
- Email: aranyabhattacharyya38@gmail.com
- LinkedIn: [linkedin.com/in/aranya-bhattacharyya](https://linkedin.com/in/aranya-bhattacharyya)
- GitHub: [@Aranya-Bhattacharyya](https://github.com/Aranya-Bhattacharyya)

---

*Last Updated: January 2026*
