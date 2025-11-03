import pandas as pd
from pathlib import Path
from analysis.data_quality_report import DataQualityReport
from datetime import datetime


class DataPipeLine:
    """Class to orchestrate the full data workflow."""

    def __init__(self, input_path: Path, output_path: Path):
        self.input_path = input_path / "world-data-2023.csv"
        self.output_path = output_path / "data_quality_report.txt"

        # Data Quality Report
        dq_report = DataQualityReport(
            input_path=self.input_path,
            output_path=self.output_path,
        )

        # Get cleaned data for further processing if needed
        self.cleaned_df = dq_report.run()

        pass

    def run(self):
        """Run the full data pipeline."""
        dq_report = DataQualityReport(
            input_path=self.input_path,
            output_path=self.output_path,
        )
        dq_report.run()
        # Example: Run data quality report
