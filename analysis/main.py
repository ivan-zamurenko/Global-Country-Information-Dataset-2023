import pandas as pd
import numpy as np
import seaborn as sns
from pathlib import Path

"""
Global Country Information Dataset 2023 - Main Analysis Module

This script serves as the entry point for analyzing the world data dataset.
"""

import matplotlib.pyplot as plt

# Set up paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_CLEANED = PROJECT_ROOT / "data" / "cleaned"
RESULTS_DIR = PROJECT_ROOT / "results"

def load_raw_data():
    """Load the raw world data CSV file."""
    data_path = DATA_RAW / "world-data-2023.csv"
    df = pd.read_csv(data_path)
    print(f"Loaded dataset with {len(df)} countries and {len(df.columns)} features")
    return df

def main():
    """Main analysis entry point."""
    # Create directories if they don't exist
    DATA_CLEANED.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load data
    df = load_raw_data()
    
    # Basic dataset info
    print("\nDataset Overview:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nFirst few rows:")
    print(df.head())

if __name__ == "__main__":
    main()