# EDA Framework

**Purpose**: Standardize data quality checks and initial profiling before deep hypothesis testing.

## 1. Data Quality Checks (The "Smell Test")
Before running any complex analysis, ensure the data is fit for purpose.

### Structural Checks
- **Shape**: `df.shape` - Does the row count match expectations?
- **Types**: `df.dtypes` - Are dates actually datetime objects? Are numeric columns not strings?
- **Uniqueness**: check primary keys are unique. `df['id'].is_unique`.

### Missingness
- **Null Counts**: `df.isnull().sum()`
- **Pattern**: Are nulls random or systematic? (e.g., all nulls in `churn_date` for active users is expected).

### Duplicates
- Check for full row duplicates.
- Check for key duplicates (one user having multiple "latest" status rows).

## 2. Univariate Distributions
Understand the baseline behavior of your variables.

### Numeric
- **Central Tendency**: Mean vs Median (Skewness check).
- **Spread**: Std Dev, IQR.
- **Outliers**: Boxplots or Z-scores (>3 std dev).
- **Visualization**: Histograms (`sns.histplot`).

### Categorical
- **Cardinality**: Number of unique values.
- **Top N**: Most frequent categories.
- **Visualization**: Bar charts (`df['col'].value_counts().plot(kind='bar')`).

## 3. Bivariate Relationships (Profiling)
Quick checks for obvious correlations.

- **Correlation Matrix**: Heatmap of numeric variables.
- **Scatter Plots**: `x` vs `y` for key metrics.
- **Box Plot**: Numeric distribution split by Category (e.g., AOV by User Tier).

## 4. Output Standards
- **Save Sudo-report**: Generate a brief markdown summary of these findings.
- **Flag Issues**: Any data quality issue must be raised immediately before proceeding to Hypothesis Testing.
