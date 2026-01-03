import pandas as pd
from src.feature_engineering import build_features
from src.ge_validation import validate_data

def test_ge_pass():
    df = pd.DataFrame({
        "loan_id": ["A1"],
        "branch_id": ["B001"],
        "filing_date": ["2024-01-01"],
        "approval_date": ["2024-01-10"]
    })

    df = build_features(df)
    res = validate_data(df)
    assert res["success"]

