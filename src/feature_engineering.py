
import pandas as pd
import holidays

US_HOLIDAYS = holidays.US()

def build_features(df):
    df["filing_date"] = pd.to_datetime(df["filing_date"])
    df["approval_date"] = pd.to_datetime(df["approval_date"], errors="coerce")

    df["days_to_approval"] = (
        df["approval_date"] - df["filing_date"]
    ).dt.days

    df["event"] = df["approval_date"].notnull().astype(int)

    end_date = df["approval_date"].fillna(pd.Timestamp.today())

    df["duration_days"] = (
        end_date - df["filing_date"]
    ).dt.days

    def holiday_count(row):
        return sum(
            1 for d in pd.date_range(row["filing_date"], end_date[row.name])
            if d.date() in US_HOLIDAYS
        )

    df["holiday_count"] = df.apply(holiday_count, axis=1)

    df["branch_load"] = (
        df.groupby("branch_id")["loan_id"]
          .transform("count")
    )

    return df
