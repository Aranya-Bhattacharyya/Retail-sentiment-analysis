Retail Customer Sentiment Analysis
An end-to-end NLP pipeline translating 568k+ customer reviews into actionable operational improvements.

Project Overview
This project automates the analysis of customer feedback using Natural Language Processing (NLP) to bridge the gap between numerical ratings and actual customer experience. By identifying "Sentiment Dissonance," the pipeline highlights specific areas for operational optimization in supply chain, packaging, and product quality.

Status: Complete

Key Findings & Results
The analysis was performed on a dataset of over 568,000 reviews, providing a statistically significant view of customer sentiment patterns.

1. Sentiment-Rating Alignment
High Model Accuracy: Successfully achieved an 80.22% agreement rate between VADER sentiment compound scores and user-provided star ratings.

Positivity Bias: Roughly 88.1% of all reviews were classified as positive, with a mean sentiment compound score of 0.94 for 5-star ratings.

2. Operational Insight: The "Sentiment Gap"
By calculating the dissonance between numerical ratings and text sentiment, the project identified critical operational blind spots:

Mismatched Positives: Identified 15,792 reviews where customers gave 4-5 stars but used strongly negative language, often related to "stale" products or packaging issues that did not affect the product's primary rating.

Mismatched Negatives: Found 45,340 reviews with 1-2 star ratings despite positive text sentiment, frequently revealing cases where customers loved the product but had a poor delivery experience—a key area for Amazon-style operational optimization.

3. Business Recommendations
Audit Logistics for "High-Gap" Products: Products identified with high rating-sentiment dissonance should undergo immediate logistics review rather than manufacturing changes, as dissatisfaction often stems from the delivery experience.

Targeted Quality Control: Use the extracted negative themes (e.g., "medicinal flavor," "weight gain") to perform targeted quality control on specific product cohorts.

Technical Approach
Data Processing
Text Cleaning: Automated removal of HTML tags, URLs, and extra whitespace.

Preprocessing: Conversion to lowercase and normalization to improve VADER accuracy.

Refinement: Removal of empty reviews following the cleaning process.

Sentiment Analysis
Method: VADER (Valence Aware Dictionary and Sentiment Reasoner) was implemented for its sensitivity to retail nuances like intensifiers ("!!!") and capitalization.

Scoring: Calculation of neg, neu, pos, and compound scores (-1 to +1).

Classification: Labels assigned as Positive (≥ 0.05), Negative (≤ -0.05), or Neutral.

Visualization & Insights
Brand Health Timelines: Tracking sentiment evolution over a 20-year period.

The "Sentiment Gap": Bar charts identifying specific Product IDs with the highest dissonance between rating and text.

Pain Point Word Clouds: Visualizing recurring themes in negative reviews for targeted QA.

Tech Stack
Languages: Python 3.13

Libraries: pandas, NumPy, VADER (vaderSentiment), Matplotlib, Seaborn, WordCloud

Environment: Jupyter Notebook

Project Structure
Retail-sentiment-analysis/
├── data/
│   ├── raw/            # Original Amazon Fine Food Reviews (Kaggle)
│   └── processed/      # Cleaned data with VADER sentiment scores
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_sentiment_analysis.ipynb
│   └── 03_visualization_and_insights.ipynb
├── results/
│   └── figures/        # Exported charts (Brand health, Gap analysis)
├── src/                # Modular Python scripts
├── README.md
└── requirements.txt
Skills Demonstrated
Applied NLP: Full pipeline implementation including text cleaning and VADER lexicon scoring.

Operational Strategy: MBA-level translation of data dissonance into actionable business value.

Data Engineering: Managing large-scale datasets (568k+ rows) and professional directory structures.

Strategic Visualization: Use of Seaborn and Matplotlib to present complex sentiment trends to stakeholders.

Contact
Aranya Bhattacharyya

Email: aranyabhattacharyya38@gmail.com

LinkedIn: linkedin.com/in/aranya-bhattacharyya

GitHub: @Aranya-Bhattacharyya
