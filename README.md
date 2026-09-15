ETHIOCHICKEN ANALYTICS
--------------------------------------------------------------------------------

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://ethio-chicken-analytics-plqeu7jazvsv8hghvcdncg.streamlit.app/)

DESCRIPTION
--------------------------------------------------------------------------------
An end-to-end data platform, statistical modeling suite, and interactive Streamlit 
web application built to optimize poultry distribution logistics, monitor chick 
mortality risks, track vaccination compliance, and segment agent performance 
across regional supply chains.

THE PROBLEM
--------------------------------------------------------------------------------
Poultry distribution networks face severe operational inefficiencies, notably 
elevated early-stage chick mortality rates averaging 6.65% across 4,196 analyzed 
cycles. Specifically, "New" tier agents experience critical mortality spikes 
reaching 12.26%, driven by onboarding gaps and inconsistent vaccination compliance 
(which averages 85.44% globally). Furthermore, regional credit risks manifested 
by high Days Sales Outstanding (DSO averaging 14.7 days) and manual tracking 
bottlenecks hinder proactive supply chain management and field intervention.

THE SOLUTION
--------------------------------------------------------------------------------
This platform delivers a comprehensive data science and analytics solution that:
- Automates data ingestion, cleaning, and metric calculation for over 1.16M 
  distributed chicks.
- Deploys L2-Regularized Logistic Regression and XGBoost models to predict high-mortality 
  risk orders exceeding the 10% threshold.
- Applies unsupervised K-Means clustering (k=4) to segment agents by behavioral 
  and performance profiles.
- Provides an interactive Streamlit operational dashboard for real-time risk monitoring, 
  regional filtering, and agent tier evaluation.

TECH STACK
--------------------------------------------------------------------------------
- Core Language: Python 3.10+
- Data Manipulation & Processing: Pandas, NumPy
- Machine Learning & Statistics: Scikit-Learn (Logistic Regression, KMeans, StandardScaler), 
  XGBoost, Statsmodels (OLS Regression), SciPy (ANOVA, Kruskal-Wallis)
- Visualization & Dashboarding: Streamlit, Plotly, Seaborn, Matplotlib
- Environment Management: Local venv with pip dependency control

RECOMMENDATIONS FOR IMPLEMENTATION
--------------------------------------------------------------------------------
1. Prioritize Onboarding Mentorship: Implement targeted brooding mentorship and 
   field support for "New" tier agents to mitigate their elevated 12.26% mortality rate.
2. Automate Compliance Enforcement: Leverage the confirmed inverse relationship 
   between vaccination compliance and mortality outcomes by integrating automated 
   compliance tracking alerts into agent workflows.
3. Tighten Credit & Financial Controls: Address elevated Days Sales Outstanding (DSO) 
   in high-risk regions by introducing stricter payment terms or integrated digital 
   micro-finance workflows.

DEVELOPED BY
--------------------------------------------------------------------------------
Aklilu Abera | Reporting Analyst
