import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import analysis.data_pipeline

"""
Global Country Information Dataset 2023 - Main Analysis Module

This script serves as the entry point for analyzing the world data dataset.
"""

# Set up paths
PROJECT_ROOT = Path(__file__).parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_CLEANED = PROJECT_ROOT / "data" / "cleaned"
RESULTS_DIR = PROJECT_ROOT / "results"

# Threshold for outlier detection based on quantiles
QUANTILE_THRESHOLD = 0.95


def main():
    """Main analysis entry point."""
    # Create directories if they don't exist
    DATA_CLEANED.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    #! Task 1: Setup the data pipeline
    analysis.data_pipeline.run_pipeline()


if __name__ == "__main__":
    main()
