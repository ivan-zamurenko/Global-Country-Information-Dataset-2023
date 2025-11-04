import pytest
import pandas as pd
from analysis.data_pipeline import (
    format_column_names,
    format_row_values,
    handle_missing_values,
    remove_outliers,
    validate_data,
    KEY_COLUMNS,
    QUANTILE_HIGH_THRESHOLD,
    QUANTILE_LOW_THRESHOLD,
)


def test_format_column_names():
    """
    Test that column names are standardized:
        - Special symbols replaced
        - Percent sign replaced with 'pct'
        - Lowercased and underscores
    """
    df = pd.DataFrame({"Col 1%": [1], "$Col-2": [2]})
    df = format_column_names(df)
    assert list(df.columns) == ["col_1pct", "col_2"]


def test_format_row_values():
    """
    Test that row values are cleaned:
        - Remove $ and % and commas
        - Convert to numeric
    """
    df = pd.DataFrame({"money": ["$1,000", "$2,500%", "300"]})
    df = format_row_values(df)
    assert df["money"].tolist() == [1000, 2500, 300]


def test_handle_missing_values():
    """
    Test missing value handling:
        - Object columns get 'Unknown' and stripped
        - Numeric columns get -1
    """
    df = pd.DataFrame({"name": [None, " Alice "], "value": [None, 5]})
    df = handle_missing_values(df)
    assert df["name"].tolist() == ["Unknown", "Alice"]
    assert pd.isna(df["value"][0]) and df["value"][1] == 5


def test_remove_outliers():
    """
    Test outlier removal:
        - Values above quantile threshold set to -1
    """
    df = pd.DataFrame({"population": [1, 2, 1000, 3, 4, -1000]})
    df = remove_outliers(
        df, ["population"], QUANTILE_HIGH_THRESHOLD, QUANTILE_LOW_THRESHOLD
    )
    # Outliers (above high quantile and below low quantile) set to NaN
    assert pd.isna(df["population"]).sum() == 2


def test_validate_data():
    """
    Test data validation:
        - Non-numeric and negative values set to -1
    """
    df = pd.DataFrame({"population": [1, -5, "bad", 10]})
    df = validate_data(df, ["population"])
    # Non-numeric and negative values set to NaN
    result = df["population"].tolist()
    assert result[0] == 1
    assert pd.isna(result[1])
    assert pd.isna(result[2])
    assert result[3] == 10
