---
name: shap
description: Model interpretability and explainability using SHAP (SHapley Additive exPlanations). Use this skill when explaining machine learning model predictions, computing feature importance, generating SHAP plots (waterfall, beeswarm, bar, scatter, force, heatmap), debugging models, analyzing model bias or fairness, comparing models, or implementing explainable AI. Works with tree-based models (XGBoost, LightGBM, Random Forest), deep learning (TensorFlow, PyTorch), linear models, and any black-box model.
---

# SHAP (SHapley Additive exPlanations)

## Overview

SHAP is a unified approach to explain machine learning model outputs using Shapley values from cooperative game theory. This skill provides comprehensive guidance for:

- Computing SHAP values for any model type
- Creating visualizations to understand feature importance
- Debugging and validating model behavior
- Analyzing fairness and bias
- Implementing explainable AI in production

## Quick Start Guide

### Step 1: Select the Right Explainer

1. **Tree-based model?** (XGBoost, LightGBM, CatBoost, Random Forest)
   - Use `shap.TreeExplainer` (fast, exact)

2. **Deep neural network?** (TensorFlow, PyTorch)
   - Use `shap.DeepExplainer` or `shap.GradientExplainer`

3. **Linear model?** (Linear/Logistic Regression)
   - Use `shap.LinearExplainer` (extremely fast)

4. **Any other model?** (SVMs, black-box)
   - Use `shap.KernelExplainer` (model-agnostic, slower)

### Step 2: Compute SHAP Values

```python
import shap
import xgboost as xgb

# Train model
model = xgb.XGBClassifier().fit(X_train, y_train)

# Create explainer
explainer = shap.TreeExplainer(model)

# Compute SHAP values
shap_values = explainer(X_test)
```

### Step 3: Visualize Results

**Global Importance (Beeswarm)**:
```python
shap.plots.beeswarm(shap_values, max_display=15)
```

**Individual Prediction (Waterfall)**:
```python
shap.plots.waterfall(shap_values[0])
```

**Feature Relationship (Scatter)**:
```python
shap.plots.scatter(shap_values[:, "Feature_Name"])
```

## Core Workflows

### Workflow 1: Basic Model Explanation
**Goal**: Understand drivers of model predictions.
1. Train model & create explainer.
2. Compute SHAP values.
3. Plot beeswarm for global view.
4. Plot waterfall for specific high-interest cases.

### Workflow 2: Model Debugging
**Goal**: Identify why a model failed on specific samples.
1. Isolate misclassified samples.
2. Run waterfall plot for those samples.
3. Check if top contributing features make sense or indicate leakage/errors.

### Workflow 3: Fairness Analysis
**Goal**: Check for bias.
1. Split data by sensitive attribute (e.g., Gender, Region).
2. Compare SHAP beeswarm plots for each group.
3. Check if sensitive attributes have high SHAP importance directly.

## Performance Optimization
- **Large Datasets**: Use `shap_values = explainer(X_test[:1000])` (sampling) if dataset is huge.
- **TreeExplainer**: Is optimized and fast for millions of rows.
- **KernelExplainer**: Is slow. Always use `kmeans` to summarize background data: `shap.KernelExplainer(model.predict, shap.kmeans(X_train, 100))`.

## Dependencies
- `shap`
- `matplotlib`
- `scikit-learn` (for data prep/models)
- `xgboost`/`lightgbm` (common use cases)
