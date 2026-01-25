# Statistical Methods

**Owner**: Data Scientist
**Purpose**: Execute rigorous statistical analysis and predictive modeling.

## 1. Financial Data Standards (Critical)
**Financial data is typically non-normal (skewed, heavy-tailed).**
- **Group Comparison**: Use **Mann-Whitney U** (not t-test).
- **Effect Size**: Use **Cliff's Delta** (not Cohen's d).
    - |δ| < 0.147: Negligible
    - |δ| ≥ 0.474: Large
- **Descriptive Stats**: Use **Median/IQR** (not mean/std).
- **Feature Selection**: Rank features by *Effect Size* (Cliff's Delta).

## 2. Method Selection Guide (Decision Logic)
**"Which test should I use?"**

### Hypothesis Testing
| Condition | Metric Type | Recommended Test |
| :--- | :--- | :--- |
| **Comparing 2 Groups** | Continuous (Normal) | T-Test (Welch's) |
| **Comparing 2 Groups** | Continuous (Non-Normal/Financial) | **Mann-Whitney U** |
| **Comparing 2 Groups** | Binary (Conversion Rate) | Chi-Square / Fisher's Exact |
| **Comparing >2 Groups** | Continuous | ANOVA (or Kruskal-Wallis) |

### Predictive Modeling
| Goal | Target Variable | Recommended Model |
| :--- | :--- | :--- |
| **Explain Drivers** | Continuous | Linear Regression (statsmodels) |
| **Explain Drivers** | Binary | Logistic Regression (statsmodels) |
| **High Accuracy** | Any | LightGBM / CatBoost |
| **Interpretation** | Any | EBM (Explainable Boosting Machine) |
**Purpose**: Validate if observed effects are statistically significant.
- **A/B Testing**:
    - **Continuous Metrics** (e.g., AOV): T-test / Mann-Whitney U.
    - **Conversion Rates**: Chi-Square / Fisher's Exact.
- **ANOVA**: Comparing means across >2 groups.

## 2. Regression & Classification
**Purpose**: Predict outcomes or explain drivers.
- **Linear Regression**: Understanding drivers of a continuous metric (e.g., "What drives LTV?").
- **Logistic Regression**: Predicting binary outcomes (e.g., Churn vs. Retain).
- **Decision Trees/Random Forest**: Non-linear relationships and feature importance.

## 3. Time Series Analysis
**Purpose**: Analyze data over time.
- **Decomposition**: Trend, Seasonality, Residuals.
- **Forecasting**: ARIMA, Prophet (for seasonal data).
- **YoY / MoM**: Growth rate calculations.

## 4. Clustering & Segmentation
**Purpose**: Group similar entities.
- **K-Means**: Behavioral segmentation based on N dimensions.
- **RFM Analysis**:
    - **Purpose**: Customer Value segmentation.
    - **Metrics**: Recency, Frequency, Monetary.
    - **Segments**: "Champions", "At Risk", "Hibernating".

## 5. Explainable AI (XAI)
**Purpose**: Interpret "Black Box" models to understand drivers of predictions.
- **SHAP (Shapley Additive Explanations)**:
    - **Detailed Usage**: See `skills/analysis/xai.md`.
    - **Global Importance**: Which features matter most overall?
    - **Local Importance**: Why did *this specific user* churn?
    - **Dependence Plots**: How does feature X impact Y (linear/non-linear)?
- **InterpretML**:
    - **EBM (Explainable Boosting Machine)**: High accuracy "glass-box" models.

## 6. Business Analytics
**Purpose**: Track behavior and identify drop-off points.
### Cohort Analysis
- **Purpose**: Track behavior of user groups over time.
- **Key Metrics**: Retention Rate, LTV, Repeat Purchase Rate.
- **Visualization**: Heatmap (Cohorts on Y-axis, Time on X-axis).

### Funnel Analysis
- **Purpose**: Identify drop-off points in a process.
- **Stages**: Sequential steps towards a goal (e.g., Sign Up -> Onboarding -> Activation, or View -> Cart -> Purchase).
- **Metric**: Conversion Rate (Step-to-Step, Overall).

### Pareto Analysis (80/20 Rule)
- **Purpose**: Prioritize factors.
- **Application**: Identify top 20% of customers driving 80% of revenue.
