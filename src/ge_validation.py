import great_expectations as ge

def validate_data(df):
    gdf = ge.from_pandas(df)

    gdf.expect_column_values_to_be_between("holiday_count", 0, 30)
    gdf.expect_column_values_to_be_between("branch_load", 1, 20000)

    gdf.expect_column_values_to_be_between(
        "days_to_approval", 0, 180,
        row_condition="days_to_approval.notnull()",
        condition_parser="pandas"
    )

    result = gdf.validate()
    assert result["success"]
    return result

