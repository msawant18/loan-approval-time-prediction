import pandas as pd
from src.feature_engineering import build_features

def test_features():
    df = pd.DataFrame({
        "loan_id": ["A1"],
        "branch_id": ["B001"],
        "filing_date": ["2024-01-01"],
        "approval_date": ["2024-01-10"]
    })

    out = build_features(df)
    assert out["days_to_approval"].iloc[0] == 9

