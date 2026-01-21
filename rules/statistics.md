# Statistical Analysis Standards

## Required Approach for Financial Data
Financial data is typically non-normal (skewed, heavy-tailed). **Always use:**

1. **Mann-Whitney U test** (not t-test) for group comparisons.
2. **Cliff's Delta** (not Cohen's d) for effect size - more robust for non-normal data.
3. **Median and IQR** (not mean and std) for descriptive statistics.

## Effect Size Interpretation (Cliff's Delta)
- |δ| < 0.147: Negligible
- 0.147 ≤ |δ| < 0.33: Small
- 0.33 ≤ |δ| < 0.474: Medium
- |δ| ≥ 0.474: Large

**Always report both p-value AND effect size.**

## Critical Practices
- Rank features by effect size (Cliff's Delta), not just p-value.
- Use `utils.eda.setup_plot_style('whitegrid', font_scale=1.0)` for consistent styling.
- **Check normality** before choosing statistical tests (Shapiro-Wilk, visual inspection).
- **Imbalanced Data**: Use stratified CV, class weights, and appropriate metrics (PR-AUC, F1, MCC).

## Modeling Considerations
- **EBM (Explainable Boosting Machine)**: Use for EDA and interpretability.
- **LightGBM/CatBoost**: Use when predictive performance is key.
- **SHAP**: Use for model-agnostic explanations.
