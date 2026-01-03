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
