\# Earnings Event Study



\*\*Live Dashboard:\*\* \[https://earnings-event-study.streamlit.app/](https://earnings-event-study.streamlit.app/)



\## Overview

An event-study analysis examining the relationship between earnings surprises and abnormal stock returns across major U.S. equities (AAPL, MSFT, TSLA, AMZN).



\## Key Findings

\- \*\*Same-day reaction (-0.230 correlation):\*\* Large earnings surprises show slight negative abnormal returns, suggesting markets front-run positive news ("buy the rumor, sell the news").

\- \*\*Post-earnings drift (+0.344 correlation):\*\* Abnormal returns over the 3 days following earnings show positive correlation with surprise magnitude, consistent with the \*\*Post-Earnings Announcement Drift (PEAD)\*\* anomaly.

\- \*\*Outlier analysis:\*\* Amazon's Q1 2025 earnings (36.9% surprise) generated significant abnormal returns, highlighting that extreme surprises may drive continued price discovery.



\## Data \& Methodology

\- \*\*Price data:\*\* Yahoo Finance via `yfinance`

\- \*\*Market benchmark:\*\* S\&P 500 (SPY) for abnormal return calculation

\- \*\*Event window:\*\* 1 day before to 3 days after earnings announcement

\- \*\*Sample:\*\* 16 earnings events across 4 companies (2024–2025)



\## Tech Stack

\- Python, pandas, yfinance, matplotlib, Streamlit

\- Data processing: custom event-study pipeline with market-adjusted returns

\- Visualization: interactive scatter plots with company-level filtering



\## Files

\- `app.py` — Streamlit dashboard source code

\- `day7\_multi\_company.py` — Data collection pipeline

\- `day8\_abnormal\_returns.py` — Market-adjusted return calculations

\- `day9\_the\_real\_correlation.py` — Statistical analysis

\- `full\_earnings\_analysis.csv` — Final dataset

\- `requirements.txt` — Dependencies



\## Author

Built as a summer research project to explore quantitative equity analysis and market microstructure.

