import random
import pandas as pd
from datetime import date, timedelta

def generate_data(n=1500):
    rows = []
    start = date(2024, 1, 1)
    branches = [f"B00{i}" for i in range(1, 6)]

    for i in range(n):
        filing = start + timedelta(days=random.randint(0, 90))
        approved = random.choice([True, False])

        approval_date = (
            filing + timedelta(days=random.randint(3, 40))
            if approved else ""
        )

        rows.append({
            "loan_id": f"S{i:04d}",
            "branch_id": random.choice(branches),
            "filing_date": filing,
            "approval_date": approval_date,
            "loan_amount": random.choice([150000, 200000, 250000, 300000])
        })

    df = pd.DataFrame(rows)
    df.to_csv(
        "data/raw/loan_applications_synthetic_1500.csv",
        index=False
    )

if __name__ == "__main__":
    generate_data()
