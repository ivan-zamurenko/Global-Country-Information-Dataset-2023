import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class DataQualityReport:
    """Assess data quality and visualize missing values."""

    def __init__(self, input_path: str, output_path: str, plot_path: str):
        self.input_path = input_path
        self.output_path = output_path
        self.plot_path = plot_path
        print(
            f"✓ Data quality report initialized with \n•input: {self.input_path} \n•output: {self.output_path} \n•plots: {self.plot_path}"
        )

    def load_data(self):
        """Load CSV data."""

        self.data = pd.read_csv(self.input_path)
        print(
            f"    Dataset contains {len(self.data)} countries and {len(self.data.columns)} features."
        )

    def examine_structure(self):
        """Write basic info and missing value stats to report."""
        self.df = self.data.copy()

        with open(self.output_path, "w") as f:
            f.write("🌍 GLOBAL COUNTRY DATASET 2023 - INITIAL ASSESSMENT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("Analyst: Ivan Zamurenko (fujibayashi)\n")
            f.write("Purpose: Initial data exploration and quality assessment\n")
            f.write("Dataset: World country statistics for 196 nations\n")
            f.write("=" * 60 + "\n")

            # Basic facts
            f.write("\n📊 BASIC DATASET INFO\n")
            f.write("-" * 30 + "\n")
            f.write(f"Countries: {self.df.shape[0]} records\n")
            f.write(f"Indicators: {self.df.shape[1]} features\n")
            f.write(f"Data points: {self.df.shape[0] * self.df.shape[1]} total\n")

            # Missing value stats
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

            # Visualizations
            self.bar_plot_missing_values()
            self.heatmap_missing_values()

            # Data types
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

            # Sample Data Preview
            f.write("\n🧾 SAMPLE DATA PREVIEW\n")
            f.write("-" * 30 + "\n")
            f.write("Key columns preview:\n")
            key_cols = ["Country", "Population", "GDP", "Life expectancy"]
            if all(col in self.df.columns for col in key_cols):
                f.write(f"{self.df[key_cols].head(5)}\n")

            # Next steps
            f.write("\n💡 NEXT STEPS RECOMMENDATIONS\n")
            f.write("-" * 30 + "\n")
            f.write("1. 🧹 Clean data format issues (remove $, %, commas)\n")
            f.write("2. 🔍 Handle missing values (strategy needed)\n")
            f.write("3. 📊 Convert string columns to numeric\n")
            f.write("4. ✅ Validate data ranges and outliers\n")

    def create_summary_table(self):
        """Save summary of missing values and types."""
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

    def bar_plot_missing_values(self):
        """Bar chart: present vs missing values."""
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
            self.plot_path + "missing_values_bar.png",
            bbox_inches="tight",
        )

        plt.show()

    def heatmap_missing_values(self):
        """Heatmap: missing values per row/column."""
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
            self.plot_path + "missing_values_heatmap.png",
            bbox_inches="tight",
        )
        plt.show()

    def run(self):
        """Run all steps for data quality report."""
        self.load_data()
        self.examine_structure()
        self.create_summary_table()
        return self.df
