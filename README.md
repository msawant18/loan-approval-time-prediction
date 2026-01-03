```bash
loan-approval-time-prediction/
│
├── data/
│   └── raw/
│       ├── loan_applications_sample.csv
│       ├── loan_applications_pending_sample.csv
│       └── loan_applications_synthetic_1500.csv
│
├── src/
│   ├── generate_synthetic_data.py
│   ├── feature_engineering.py
│   ├── ge_validation.py
│   ├── drift_checks.py
│   ├── train_model.py
│   └── airflow_dag.py
│
├── tests/
│   ├── test_feature_engineering.py
│   └── test_ge_validation.py
│
├── drawio/
│   └── architecture.drawio
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```
# Loan Approval Time Prediction

ML pipeline to predict how long a loan application takes to get approved using explainable operational features.

## Problem
Banks need accurate approval time estimates to:
- Meet SLAs
- Manage branch workload
- Improve customer experience

## Target
days_to_approval = approval_date − filing_date

## Features
- holiday_count: number of public holidays during processing
- branch_load: number of loans handled by a branch

## Architecture
Airflow → Feature Engineering → Great Expectations →
Drift Detection → Model Training → Feature Importance →
MLflow Tracking → Model Registry

## Tech Stack
Python, Pandas  
LightGBM  
Great Expectations  
MLflow  
Apache Airflow  

## Data
All datasets are synthetic and safe for public use.

## Run
```bash
pip install -r requirements.txt
pytest
python src/generate_synthetic_data.py
