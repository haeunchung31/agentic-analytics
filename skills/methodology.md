# Analysis Methodologies

## Exploratory Data Analysis (EDA)
**Purpose**: Understand data structure, quality, and initial patterns.
- **Univariate**: Histograms, Distplots (Distribution shape, Skewness).
- **Bivariate**: Scatter plots, Correlation Matrices (Relationships).
- **Outlier Detection**: Z-Score, IQR Method.

## Statistical Hypothesis Testing
**Purpose**: Validate if observed effects are statistically significant.
- **A/B Testing**:
    - **Continuous Metrics** (e.g., AOV): T-test / Mann-Whitney U.
    - **Conversion Rates**: Chi-Square / Fisher's Exact.
- **ANOVA**: Comparing means across >2 groups.

## Regression & Classification
**Purpose**: Predict outcomes or explain drivers.
- **Linear Regression**: Understanding drivers of a continuous metric (e.g., "What drives LTV?").
- **Logistic Regression**: Predicting binary outcomes (e.g., Churn vs. Retain).
- **Decision Trees/Random Forest**: Non-linear relationships and feature importance.

## Time Series Analysis
**Purpose**: Analyze data over time.
- **Decomposition**: Trend, Seasonality, Residuals.
- **Forecasting**: ARIMA, Prophet (for seasonal data).
- ** YoY / MoM**: Growth rate calculations.

## Clustering & Segmentation
**Purpose**: Group similar entities.
- **K-Means**: Behavioral segmentation based on N dimensions.
- **RFM Analysis**:
    - **Purpose**: Customer Value segmentation.
    - **Metrics**: Recency, Frequency, Monetary.
    - **Segments**: "Champions", "At Risk", "Hibernating".

## Explainable AI (XAI)
**Purpose**: interpret "Black Box" models to understand drivers of predictions.
- **SHAP (Shapley Additive Explanations)**:
    - **Global Importance**: Which features matter most overall?
    - **Local Importance**: Why did *this specific user* churn?
    - **Dependence Plots**: How does feature X impact Y (linear/non-linear)?
- **InterpretML**:
    - **EBM (Explainable Boosting Machine)**: High accuracy "glass-box" models.
    - **Dashboarding**: Interactive widgets for exploring model behavior.

## Business Frameworks
### Cohort Analysis
**Purpose**: Track behavior of user groups over time.
- **Key Metrics**: Retention Rate, LTV, Repeat Purchase Rate.
- **Visualization**: Heatmap (Cohorts on Y-axis, Time on X-axis).

### Funnel Analysis
**Purpose**: Identify drop-off points in a process.
- **Stages**: View -> Add to Cart -> Checkout -> Purchase.
- **Metric**: Conversion Rate (Step-to-Step, Overall).

### Pareto Analysis (80/20 Rule)
**Purpose**: Prioritize factors.
- **Application**: Identify top 20% of customers driving 80% of revenue.
