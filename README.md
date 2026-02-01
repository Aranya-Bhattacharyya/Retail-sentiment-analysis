![Python CI](https://github.com/Aranya-Bhattacharyya/Retail-sentiment-analysis/actions/workflows/python-tests.yml/badge.svg)

Bridging the Gap Between Customer Text and Numerical Ratings
This project implements a professional NLP pipeline to process over 568,000 Amazon reviews. By identifying "Sentiment Dissonance," this tool highlights operational blind spots in logistics, packaging, and product quality—translating raw data into actionable business strategy.

Key Findings and Impact
High Model Accuracy: Achieved an 80.22% agreement rate between VADER sentiment scores and user star ratings.

Operational Blind Spots: Identified 45,340 reviews where customers liked the product but had a poor delivery experience, characterized by high rating-sentiment dissonance.

Positivity Bias: Roughly 88.1% of all reviews were classified as positive, with a mean sentiment compound score of 0.94 for 5-star ratings.

Professional Project Structure
This repository has been refactored from a research notebook into a modular Python package to meet industry software engineering standards:

Retail-sentiment-analysis/
├── src/                # Modular Source Code
│   ├── analyzer.py     # Core VADER sentiment logic
│   ├── data_processing.py
│   └── visualization.py
├── tests/              # Automated Testing Suite (Pytest)
├── Notebooks/          # Exploratory Data Analysis (EDA)
├── pyproject.toml      # Project Configuration & Tooling
└── README.md

Technical Stack and Engineering Standards
Languages: Python 3.13.

Libraries: pandas, NumPy, vaderSentiment, Matplotlib, Seaborn, and WordCloud.

Testing: Automated unit testing via Pytest.

Code Quality: PEP 8 compliance enforced with Black formatting and Flake8 linting.

Dependency Management: Modern pyproject.toml architecture used for environment reproducibility.

Installation and Usage

1. Setup Environment

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -e .

2. Running Automated Tests

Verify the reliability of the sentiment logic and data processing:

pytest

Business Recommendations

1. Audit Logistics for High-Gap Products: Products identified with high rating-sentiment dissonance should undergo immediate logistics review, as dissatisfaction often stems from the delivery experience rather than manufacturing.

2. Targeted Quality Control: Utilize recurring negative themes extracted via word clouds (e.g., "packaging issues") to perform targeted quality control on specific product cohorts.

Contact
Aranya Bhattacharyya LinkedIn: linkedin.com/in/aranya-bhattacharyya

GitHub: @Aranya-Bhattacharyya

Email: aranyabhattacharyya38@gmail.com
