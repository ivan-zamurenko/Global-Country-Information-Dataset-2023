import pandas as pd
from pathlib import Path
from analysis.data_quality_report import DataQualityReport
# You would also import your cleaning and feature engineering modules:
# from analysis.data_cleaning import clean_data
# from analysis.feature_engineering import add_features

# -----------------------------
# Data Pipeline for Country Dataset
# -----------------------------

RAW_PATH = "data/raw/world-data-2023.csv"  # Path to raw input CSV
REPORT_PATH = (
    "results/task-a/reports/data_quality_report.txt"  # Data quality report output
)
PLOT_PATH = "results/task-a/plots/"  # Directory for plots
CLEANED_PATH = "data/cleaned/world_data_2023_cleaned.csv"  # Output for cleaned data

QUANTILE_HIGH_THRESHOLD = 0.95  # Outlier threshold (upper quantile)
QUANTILE_LOW_THRESHOLD = 0.05  # Outlier threshold (lower quantile)

# Columns most critical for analysis and cleaning
KEY_COLUMNS = [
    "population",
    "land_area_km2",
    "gdp",
    "life_expectancy",
    "density_p_km2",
    "birth_rate",
    "armed_forces_size",
    "infant_mortality",
    "maternal_mortality_ratio",
    "urban_population",
    "physicians_per_thousand",
]


def run_pipeline():
    """
    Main pipeline runner for country dataset analysis.
    Steps:
        1. Assess data quality and generate report/plots
        2. Clean data (column/row formatting, missing/outlier handling, validation)
        3. Feature engineering (placeholder)
        4. Save cleaned data to output
    """
    # 1. Data Quality Assessment
    try:
        dq_report = DataQualityReport(RAW_PATH, REPORT_PATH, PLOT_PATH)
        dq_report.run()
        df = dq_report.data
        log_action(" ✔︎ Data quality report generated")
    except Exception as e:
        log_action(f" ✘ Data quality report generation failed: {e}")
        return

    # 2. Data Cleaning (calls modular cleaning functions below)
    try:
        df_cleaned = clean_data(df)
    except Exception as e:
        log_action(f" ✘ Data cleaning failed: {e}")
        return

    # 3. Feature Engineering (currently a placeholder)
    df_featured = df_cleaned.copy()

    # 4. Save cleaned data
    # df_featured.to_csv(CLEANED_PATH, index=False)
    save_cleaned_data(df_cleaned, CLEANED_PATH)
    print(f"Pipeline complete! Cleaned data saved to {CLEANED_PATH}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run all cleaning steps in order:
        - Format column names
        - Clean row values (remove symbols, convert types)
        - Handle missing values
        - Remove outliers in key columns
        - Validate data (convert to numeric, set invalids to -1)
    Returns cleaned DataFrame.
    """
    df = format_column_names(df)
    df = format_row_values(df)
    # df = handle_missing_values(df)
    df = remove_outliers(
        df, KEY_COLUMNS, QUANTILE_HIGH_THRESHOLD, QUANTILE_LOW_THRESHOLD
    )
    df = validate_data(df, KEY_COLUMNS)
    log_action(" ✔︎ Data cleaning completed")
    return df


def format_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names:
      - Replace special symbols with underscores
      - Collapse multiple underscores
      - Remove leading underscores
      - Replace % with 'pct'
      - Replace spaces with underscores
      - Strip whitespace and lowercase
    """
    df.columns = (
        df.columns.str.replace("\n", "", regex=False)
        .str.replace(r"[()\-/\$]", "_", regex=True)  # Replace symbols
        .str.replace("%", "pct")  # Replace percent sign
        .str.replace(" ", "_")  # Replace spaces
        .str.replace(r"_+", "_", regex=True)  # Collapse underscores
        .str.lstrip("_")  # Remove leading underscores
        .str.strip("_")  # Strip underscores
        .str.strip()
        .str.lstrip()
        .str.lower()  # Lowercase
    )
    log_action(" ✔︎ Formatted column names")
    return df


def format_row_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean string values in all object columns:
      - Remove currency symbols ($), percent signs (%), and commas
      - Convert cleaned strings to numeric types
    """
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.replace(r"[$%,]", "", regex=True)
        # Try to convert to numeric, but keep as string if mostly non-numeric
        converted = pd.to_numeric(df[column], errors="coerce")
        # If at least 80% of the values are numeric, convert column
        if converted.notna().sum() >= 0.8 * len(df):
            df[column] = converted
    log_action(" ✔︎ Formatted row values")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values:
      - For object columns: fill with 'Unknown' and strip whitespace
      - For numeric columns: fill with -1
    """
    for column in df.columns:
        if df[column].dtype == object:
            df[column] = df[column].fillna("Unknown").str.strip()
        # For numeric columns, leave missing values as NaN (do nothing)
    log_action(" ✔︎ Handled missing values")
    return df


def remove_outliers(
    df: pd.DataFrame,
    key_columns: list,
    quantile_high_threshold: float,
    quantile_low_threshold: float,
) -> pd.DataFrame:
    """
    For each key column, set values above the quantile threshold to -1 (mark as outlier).
    """
    for col in key_columns:
        if col in df.columns:
            upper_limit = df[col].quantile(quantile_high_threshold)
            lower_limit = df[col].quantile(quantile_low_threshold)
            df.loc[df[col] > upper_limit, col] = pd.NA
            df.loc[df[col] < lower_limit, col] = pd.NA
    log_action(" ✔︎ Removed outliers")
    return df


def validate_data(df: pd.DataFrame, key_columns: list) -> pd.DataFrame:
    """
    For each key column:
      - Convert to numeric (invalids become NaN)
      - Fill NaN with -1
      - Set negative values to -1
    """
    for col in key_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            # Do not fillna(-1); keep missing values as NaN
            df.loc[df[col] < 0, col] = pd.NA
    log_action(" ✔︎ Data validation completed")
    return df


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder for feature engineering logic.
    Extend this function to add derived columns/features.
    """
    return df


def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the cleaned DataFrame to a CSV file.
    """
    df.to_csv(output_path, index=False)
    log_action(f" ✔︎ Cleaned data saved to {output_path}")


# -----------------------------
# Logging Utility
def log_action(message, log_path="results/task-a/reports/pipeline_steps.log"):
    with open(log_path, "a") as f:
        f.write(f"{pd.Timestamp.now()}: {message}\n")


if __name__ == "__main__":
    # Entry point for running the pipeline from command line
    run_pipeline()
