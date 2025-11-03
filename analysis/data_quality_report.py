import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class DataQualityReport:
    """Class cleaning and reporting on data quality issues."""

    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        print(
            f"✓ Data quality report initialized with \n•input: {self.input_path} \n•output: {self.output_path}"
        )

    def load_data(self):
        """Load data into the report."""

        self.data = pd.read_csv(self.input_path)
        print(
            f"    Dataset contains {len(self.data)} countries and {len(self.data.columns)} features."
        )

    def examine_structure(self):
        """Examine dataset structure and report findings."""
        self.df = self.data.copy()

        with open(self.output_path, "w") as f:
            f.write("🌍 GLOBAL COUNTRY DATASET 2023 - INITIAL ASSESSMENT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("Analyst: Ivan Zamurenko (fujibayashi)\n")
            f.write("Purpose: Initial data exploration and quality assessment\n")
            f.write("Dataset: World country statistics for 196 nations\n")
            f.write("=" * 60 + "\n")

            # ! Basic Facts
            f.write("\n📊 BASIC DATASET INFO\n")
            f.write("-" * 30 + "\n")
            f.write(f"Countries: {self.df.shape[0]} records\n")
            f.write(f"Indicators: {self.df.shape[1]} features\n")
            f.write(f"Data points: {self.df.shape[0] * self.df.shape[1]} total\n")

            # ! Health check
            missing_ptc = (
                self.df.isnull().sum().sum() / (self.df.shape[0] * self.df.shape[1])
            ) * 100
            f.write(
                f"Completeness: {100 - missing_ptc:.2f}% ({missing_ptc:.2f}% missing)\n"
            )
            missing_values = self.df.isnull().sum()
            for column, count in missing_values.items():
                if count > 0:
                    f.write(f" ‼️ {column}: {count} missing values\n")
            if missing_values.sum() == 0:
                f.write("✅ No missing values detected.\n")

            #! Visualize missing values
            self.bar_plot_missing_values()
            self.heatmap_missing_values()

            # ! Content scan
            f.write("\n📋 CONTENT OVERVIEW\n")
            f.write("-" * 30 + "\n")
            f.write(
                f"Text columns: {len(self.df.select_dtypes(include=['object']).columns)}\n"
            )
            f.write(
                f"Numeric columns: {len(self.df.select_dtypes(include=['number']).columns)}\n"
            )
            f.write(
                f"Date columns: {len(self.df.select_dtypes(include=['datetime']).columns)}\n"
            )

            # ! Data Format Issues
            f.write("\n🧹 DATA FORMAT ISSUES\n")
            f.write("-" * 30 + "\n")
            f.write(" Cleaning columns names to standard format...\n")
            self.df.columns = (
                self.df.columns.str.strip()
                .str.lower()
                .str.replace("%", "pct")
                .str.replace(r"[ \n\(\)/\-]", "_", regex=True)
                .str.replace(r"_+", "_", regex=True)
                .str.rstrip("_")
            )
            f.write("✅ Columns cleaned. Now let's clean values...\n")
            for col in self.df.columns:
                if self.df[col].dtype == "object":
                    if self.df[col].str.contains(r"[%$]", regex=True).any():
                        f.write(f"  ❕ Cleaning format issues in column: {col}\n")
                        self.df[col] = (
                            self.df[col]
                            .str.replace(r"[$,]", "", regex=True)
                            .str.replace("%", "")
                            .astype(float)
                        )
            f.write("✅ Data format cleaning completed.\n")

            # ! Sample Data Preview
            f.write("\n🧾 SAMPLE DATA PREVIEW\n")
            f.write("-" * 30 + "\n")
            f.write("Key columns preview:\n")
            key_cols = ["country", "abbreviation", "land_area_km2", "population"]
            if all(col in self.df.columns for col in key_cols):
                f.write(f"{self.df[key_cols].head(5)}\n")

            # ! Recommendations
            f.write("\n💡 NEXT STEPS RECOMMENDATIONS\n")
            f.write("-" * 30 + "\n")
            f.write("1. 🧹 Clean data format issues (remove $, %, commas)\n")
            f.write("2. 🔍 Handle missing values (strategy needed)\n")
            f.write("3. 📊 Convert string columns to numeric\n")
            f.write("4. ✅ Validate data ranges and outliers\n")

    def create_summary_table(self):
        """Create a summary table of data quality issues."""
        df = self.data.copy()

        # Create summary table
        summary_data = []
        for col in df.columns:
            summary_data.append(
                {
                    "Column": col,
                    "Data_Type": str(df[col].dtype),
                    "Missing_Count": df[col].isnull().sum(),
                    "Missing_Percent": f"{(df[col].isnull().sum() / len(df)) * 100:.2f}%",
                }
            )

        summary_df = pd.DataFrame(summary_data)
        summary_df.to_csv(
            str(self.output_path).replace(".txt", "_summary.csv"), index=False
        )

    #! Missing values plotting could be added here in future iterations
    def bar_plot_missing_values(self):
        """Plot missing values bar chart & heatmap."""
        missing_values_pct = self.df.isnull().sum() / len(self.df)
        present_values_pct = 1 - missing_values_pct

        # Bar plot
        plt.figure(figsize=(20, 12))
        columns = self.df.columns
        x = np.arange(len(columns))

        # blue bar plot
        plt.bar(x, present_values_pct, color="blue", label="Present Values %")

        # red bar plot
        plt.bar(x, missing_values_pct, color="red", label="Missing Values %")
        plt.xticks(x, columns, rotation=90)
        plt.ylim(0, 1)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.ylabel("Proportion of data")
        plt.title("Data Completeness")
        plt.legend()
        plt.tight_layout()

        plt.savefig(
            str(self.output_path).replace(".txt", "_missing_values_bar.png"),
            bbox_inches="tight",
        )

        plt.show()

    def heatmap_missing_values(self):
        """Plot missing values heatmap"""
        plt.figure(figsize=(20, 12))
        sns.heatmap(
            self.df.isnull(),
            cmap="Reds",
            cbar=True,
            yticklabels=False,
            linewidths=0.5,
            linecolor="gray",
            vmin=0,
            vmax=1,
        )
        plt.title("Missing Values Heatmap", fontsize=18)
        plt.xlabel("Features", fontsize=14)
        plt.ylabel("Rows (samples)", fontsize=12)
        plt.tight_layout()
        plt.savefig(
            str(self.output_path).replace(".txt", "_missing_values_heatmap.png"),
            bbox_inches="tight",
        )
        plt.show()
        pass

    def run(self):
        """Run the data quality report generation."""
        self.load_data()
        self.examine_structure()
        self.create_summary_table()
        return self.df
