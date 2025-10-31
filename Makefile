.PHONY: install clean explore notebook clean-data stats

install:
	conda install -c conda-forge pandas numpy matplotlib seaborn plotly jupyter

explore:
	@python3 -c "import pandas as pd; df = pd.read_csv('data/raw/world-data-2023.csv'); print(f'Shape: {df.shape}'); print('Columns:', df.columns.tolist()[:10], '...'); print('\nSample:'); print(df[['Country', 'Population', 'GDP', 'Life expectancy']].head(3))"

notebook:
	cd notebooks && jupyter notebook

clean-data:
	@mkdir -p data/cleaned
	@python3 -c "import pandas as pd; df = pd.read_csv('data/raw/world-data-2023.csv'); df.to_csv('data/cleaned/world_data_2023_cleaned.csv', index=False); print('✓ Cleaned data saved')"

stats:
	@python3 -c "import pandas as pd; df = pd.read_csv('data/raw/world-data-2023.csv'); print(f'Countries: {len(df)}, Features: {len(df.columns)}, Missing: {df.isnull().sum().sum()}')"

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name ".DS_Store" -delete