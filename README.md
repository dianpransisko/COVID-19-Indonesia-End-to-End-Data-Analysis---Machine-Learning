📊 COVID-19 Indonesia: End-to-End Data Analysis & Machine Learning
This project delivers a comprehensive analysis of the COVID-19 pandemic's evolution in Indonesia (March 2020 – September 2022). It covers the full data lifecycle—from advanced PostgreSQL data wrangling and statistical analysis to Machine Learning implementation for regional risk stratification and fatality prediction.

Primary Data Source: COVID-19 Indonesia Dataset by Hendratno via Kaggle.

Original Data License: CC BY-NC-SA 4.0

Usage Policy: In compliance with the ShareAlike (SA) provision, all analyses, source code (Python & SQL), and modeling outputs in this repository are also licensed under CC BY-NC-SA 4.0.

🚀 Objectives
- Analyze transmission and fatality trends at both national and provincial levels.
- Identify high-risk geographical zones using Clustering techniques.
- Construct Regression models to quantify the correlation between new cases and mortality rates.

🛠️ Technological Stack
- Database: PostgreSQL (Advanced Wrangling, Aggregations, Window Functions).
- Programming: Python 3.10.
- Libraries: Pandas, NumPy, Matplotlib, Seaborn.
- Machine Learning: Scikit-Learn (Linear Regression, K-Means Clustering, StandardScaler).

- 📉 Workflow
1. Data Ingestion & SQL Processing
- Raw datasets (CSV) were migrated to PostgreSQL for robust cleaning and transformation. Key SQL techniques include:
- Window Functions (LAG, AVG OVER): Utilized to calculate daily case variances and 7-Day Moving Averages.
- Data Aggregation: Summarizing cumulative statistics across 34 provinces.
