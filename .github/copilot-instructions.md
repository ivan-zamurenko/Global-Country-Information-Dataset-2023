# Global Country Information Dataset 2023 - AI Coding Agent Instructions

## Project Overview
This is a data science project for analyzing global country information using a comprehensive 2023 dataset (`data/raw/world-data-2023.csv`) containing 196 countries with 35 indicators including demographics, economics, geography, and social metrics.

## Data Architecture

### Core Dataset Structure
- **Source**: `data/raw/world-data-2023.csv` (196 countries × 35 features)
- **Key Fields**: Country, Population, GDP, Life expectancy, Education enrollment, CO2 emissions, Geographic coordinates, Economic indicators (CPI, tax rates, unemployment), Health metrics, Agricultural/forested land percentages
- **Data Processing Flow**: `data/raw/` → `data/cleaned/` → `analysis/` → `results/task-{x}/`

### Directory Structure Conventions
```
analysis/          # Analysis scripts and modules
data/
  raw/            # Original, immutable datasets
  cleaned/        # Processed, analysis-ready data
notebooks/        # Jupyter notebooks for exploration
results/
  task-a/         # Organized by analysis task/question
    plots/        # Visualizations output
    reports/      # Generated analysis reports
sql/              # Database queries and schema
tests/            # Data validation and unit tests
```

## Development Patterns

### Data Processing Workflow
1. **Raw Data**: Always preserve original `world-data-2023.csv` untouched
2. **Cleaning**: Output cleaned datasets to `data/cleaned/` with descriptive names
3. **Analysis**: Create task-specific folders under `results/` (e.g., `task-b`, `task-demographic-analysis`)
4. **Outputs**: Separate plots and reports within each task folder

### File Naming Conventions
- Analysis scripts: `{task_name}_analysis.py` or `{metric}_exploration.py`
- Cleaned data: `world_data_2023_cleaned.csv`, `gdp_normalized.csv`
- Plots: `{metric}_{chart_type}.png` (e.g., `gdp_scatter_plot.png`)
- Reports: `{task_name}_report.md` or `{analysis_type}_summary.pdf`

### Data Handling Best Practices
- Use pandas for CSV operations; handle missing values explicitly
- For geographic analysis, leverage `Latitude`/`Longitude` columns
- Economic data contains currency symbols and commas - clean before numeric operations
- Population and GDP values are formatted strings requiring parsing
- Percentage fields need string cleaning (remove '%' symbol)

### Common Analysis Patterns
- **Correlation Analysis**: Focus on GDP vs Life Expectancy, Education vs Development metrics
- **Geographic Clustering**: Use lat/long for regional comparisons
- **Economic Indicators**: Combine GDP, tax rates, unemployment for economic health scoring
- **Environmental Analysis**: CO2 emissions vs population density, forested area relationships

### Technology Stack Recommendations
- **Data Processing**: pandas, numpy for core data manipulation
- **Visualization**: matplotlib, seaborn for statistical plots; plotly for interactive maps
- **Statistical Analysis**: scipy, scikit-learn for advanced analytics
- **Geographic Analysis**: geopandas, folium for mapping capabilities
- **Reporting**: matplotlib + pandas for automated report generation

### Quality Assurance
- Validate country counts (should be ~196 records)
- Check for data completeness across key indicators
- Verify geographic coordinates fall within valid ranges
- Cross-reference economic indicators for logical consistency

## Integration Points
- CSV-based workflow; consider SQLite for complex queries in `sql/`
- Coordinate outputs between `analysis/` scripts and `results/` structure
- Maintain data lineage from raw → cleaned → analysis → results