import pandas as pd
from pathlib import Path

from analysis.data_quality_report import DataQualityReport

"""
Global Country Information Dataset 2023 - Main Analysis Module

This script serves as the entry point for analyzing the world data dataset.
"""

# Set up paths
PROJECT_ROOT = Path(__file__).parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_CLEANED = PROJECT_ROOT / "data" / "cleaned"
RESULTS_DIR = PROJECT_ROOT / "results"


def main():
    """Main analysis entry point."""
    # Create directories if they don't exist
    DATA_CLEANED.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    #! Task 1: Data Cleaning
    dq_report = DataQualityReport(
        input_path=DATA_RAW / "world-data-2023.csv",
        output_path=RESULTS_DIR / "data_quality_report.txt",
    )
    dq_report.run()


if __name__ == "__main__":
    main()
