
<img width="1800" height="1200" alt="laporan_final_covid_clean" src="https://github.com/user-attachments/assets/fbdd9044-0387-4e4b-ad82-d387da73fd20" />

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
2. Exploratory Data Analysis (EDA)
- Identified critical milestones and anomalies:
- Pandemic Peak: February 16, 2022 (Omicron Wave), exceeding 64k cases/day.
- Epicenter: DKI Jakarta recorded the highest volume (1.4M+ cases).
- Fatality Anomaly: Lampung exhibited the highest Case Fatality Rate (CFR) at 5.55%.
3. Machine Learning Implementation
- Regression Analysis: Developed a predictive framework to estimate mortality based on case surges:
$$y = 0.0188x + 40$$
(where $y$ is predicted deaths and $x$ is new cases).
- K-Means Clustering: Segmented 34 provinces into 3 distinct risk zones (High Transmission, High Fatality, and Stable) to facilitate targeted policy interventions.

🖼️ Visualizations & Dashboards
The analysis provides visual insights into:
- Daily Trends vs. Moving Averages for noise reduction.
- Top 10 Provinces ranked by total case volume.
- Clustering Geospatial Maps illustrating regional risk levels.

💡 Strategic Insights & Recommendations (BI)
- Insight: High-transmission regions (e.g., Jakarta) maintain lower CFRs compared to moderate-transmission regions (e.g., Lampung), indicating disparities in medical infrastructure readiness.
- Recommendation: Prioritize the allocation of oxygen logistics and ventilators to Cluster 2 (High Fatality) regions to effectively mitigate daily mortality rates.


📂 Getting Started
1. Clone the repository:

## 🚀 Installation & Setup
1. **Clone the repository**:
   ```bash
    git clone https://github.com/yourusername/covid19-indonesia.git cd covid19-indonesia

3. Install dependencies:
Bash
pip install -r requirements.txt
Database Configuration:

4. Execute scripts in the /sql directory to set up your PostgreSQL environment.
Update database credentials in the .ipynb notebooks before execution.

📝 Citation
If you utilize this analysis or code in your research, please cite it as:
DIAN PRANSISKO HARAHAP(2026). COVID-19 Indonesia: End-to-End Data Analysis & Machine Learning. Zenodo. [ZENODO LINK]
