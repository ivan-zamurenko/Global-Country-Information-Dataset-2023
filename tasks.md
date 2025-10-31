# Data Analysis Practice Tasks - Global Country Dataset 2023
*Build Your Portfolio with Real-World Data Analysis Skills*

## 📊 Dataset Overview
**196 countries** with **35 indicators** covering:
- Demographics (Population, Birth Rate, Life Expectancy)
- Economics (GDP, Unemployment, Tax Revenue)
- Geography (Land Area, Coordinates, Population Density)
- Social (Education, Healthcare, Infrastructure)
- Environment (CO2 Emissions, Agricultural Land, Forest Coverage)

---

## 🎯 **LEVEL 1: Data Foundation Skills**
*Master the basics that every data analyst needs*

### Task 1.1: Data Quality Assessment
**Goal**: Identify and document data quality issues
- [ ] Load the dataset and examine its structure
- [ ] Create a data quality report showing:
  - Missing values count per column
  - Data types for each column
  - Columns with formatting issues (%, $, commas)
- [ ] **Deliverable**: `data_quality_report.py` + summary table

### Task 1.2: Data Cleaning Pipeline
**Goal**: Clean and prepare data for analysis
- [ ] Remove/convert currency symbols from GDP, wages, gas prices
- [ ] Convert percentage strings to numeric values
- [ ] Handle missing values (document your strategy)
- [ ] Standardize column names (remove spaces, special characters)
- [ ] **Deliverable**: `clean_data.py` + cleaned CSV file

### Task 1.3: Exploratory Data Analysis (EDA)
**Goal**: Generate insights through statistical summaries
- [ ] Calculate descriptive statistics for numeric columns
- [ ] Identify top/bottom 10 countries for key metrics
- [ ] Find correlations between major indicators
- [ ] **Deliverable**: `eda_summary.py` + findings document

---

## 🚀 **LEVEL 2: Visualization & Storytelling**
*Create compelling visual narratives*

### Task 2.1: Economic Analysis Dashboard
**Goal**: Visualize global economic patterns
- [ ] GDP vs Population scatter plot with continent colors
- [ ] Top 20 countries by GDP per capita bar chart
- [ ] Unemployment rate distribution histogram
- [ ] Tax burden vs Economic development correlation
- [ ] **Deliverable**: `economic_dashboard.py` + 4 publication-ready plots

### Task 2.2: Quality of Life Index
**Goal**: Create a composite indicator
- [ ] Build a Quality of Life score using:
  - Life expectancy (weight: 30%)
  - Education enrollment (weight: 25%)
  - Healthcare access (weight: 25%)
  - Economic prosperity (weight: 20%)
- [ ] Rank countries and visualize results
- [ ] **Deliverable**: `quality_of_life_index.py` + interactive ranking

### Task 2.3: Geographic Data Visualization
**Goal**: Master geospatial analysis
- [ ] Create world maps showing:
  - Population density
  - CO2 emissions per capita
  - Life expectancy
- [ ] Build an interactive map with multiple layers
- [ ] **Deliverable**: `geographic_analysis.py` + interactive HTML maps

---

## 🔥 **LEVEL 3: Advanced Analytics**
*Develop machine learning and advanced statistical skills*

### Task 3.1: Country Clustering Analysis
**Goal**: Segment countries using unsupervised learning
- [ ] Perform K-means clustering using economic/social indicators
- [ ] Determine optimal number of clusters
- [ ] Profile each cluster with key characteristics
- [ ] Validate clusters with geographic/regional patterns
- [ ] **Deliverable**: `country_clustering.py` + cluster interpretation report

### Task 3.2: Predictive Modeling
**Goal**: Build and evaluate prediction models
- [ ] Predict life expectancy using economic/social factors
- [ ] Try multiple algorithms (Linear Regression, Random Forest, etc.)
- [ ] Evaluate model performance with cross-validation
- [ ] Feature importance analysis
- [ ] **Deliverable**: `life_expectancy_model.py` + model evaluation report

### Task 3.3: Statistical Hypothesis Testing
**Goal**: Apply rigorous statistical methods
- [ ] Test: "Wealthier countries have better healthcare outcomes"
- [ ] Test: "Countries with higher education spending have lower unemployment"
- [ ] Control for confounding variables
- [ ] Report confidence intervals and effect sizes
- [ ] **Deliverable**: `hypothesis_testing.py` + statistical findings report

---

## 💼 **LEVEL 4: Business Intelligence**
*Real-world business applications*

### Task 4.1: Investment Attractiveness Score
**Goal**: Create a business decision-making tool
- [ ] Build composite score considering:
  - Economic stability (GDP growth, inflation)
  - Business environment (tax rates, infrastructure)
  - Human capital (education, healthcare)
  - Market size (population, urbanization)
- [ ] **Deliverable**: `investment_analysis.py` + executive summary dashboard

### Task 4.2: Risk Assessment Framework
**Goal**: Identify country-level risks
- [ ] Economic risk indicators
- [ ] Social stability metrics
- [ ] Environmental sustainability factors
- [ ] Create risk categories and warning systems
- [ ] **Deliverable**: `risk_assessment.py` + risk monitoring dashboard

### Task 4.3: Market Opportunity Analysis
**Goal**: Identify emerging markets
- [ ] Analyze population growth + economic indicators
- [ ] Identify undervalued markets with growth potential
- [ ] Create market entry recommendations
- [ ] **Deliverable**: `market_analysis.py` + strategic recommendations

---

## 📈 **LEVEL 5: Advanced Portfolio Projects**
*Stand-out projects for senior positions*

### Task 5.1: Automated Reporting System
**Goal**: Build production-ready analytics
- [ ] Create automated reports that update with new data
- [ ] Build PDF report generation
- [ ] Implement data validation and quality checks
- [ ] **Deliverable**: End-to-end reporting pipeline

### Task 5.2: Interactive Web Dashboard
**Goal**: Full-stack analytics application
- [ ] Build web interface for data exploration
- [ ] Real-time filtering and visualization
- [ ] Export functionality for insights
- [ ] **Deliverable**: Deployed web application

### Task 5.3: Research Paper
**Goal**: Academic-level analysis
- [ ] Choose research question (e.g., "Factors affecting sustainable development")
- [ ] Rigorous methodology and statistical analysis
- [ ] Publication-quality visualizations
- [ ] **Deliverable**: 15-page research paper with code appendix

---

## 🛠 **Technical Skills You'll Master**

### Data Manipulation
- pandas, numpy for data processing
- Data cleaning and transformation
- Handling missing data and outliers

### Visualization
- matplotlib, seaborn for statistical plots
- plotly for interactive visualizations
- Geographic mapping with folium/geopandas

### Statistics & ML
- scipy for statistical testing
- scikit-learn for machine learning
- Model evaluation and validation

### Business Intelligence
- KPI development and tracking
- Dashboard creation
- Executive reporting

---

## 🎯 **Portfolio Building Tips**

1. **Document Everything**: Each task should have clear README with methodology
2. **Show Your Process**: Include failed attempts and lessons learned
3. **Business Context**: Always connect technical findings to real-world implications
4. **Code Quality**: Clean, commented, and reproducible code
5. **Visual Excellence**: Publication-ready plots with proper styling

## 📁 **Recommended File Structure**
```
analysis/
├── level_1_foundation/
├── level_2_visualization/
├── level_3_advanced/
├── level_4_business/
├── level_5_portfolio/
results/
├── plots/
├── reports/
├── dashboards/
```

**Start with Level 1 and progress systematically. Each level builds on previous skills!**