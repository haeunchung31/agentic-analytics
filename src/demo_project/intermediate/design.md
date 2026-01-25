---
type: design
status: draft
project: demo_project
brainstorm_ref: src/demo_project/intermediate/brainstorm.md
---

# Technical Design: Q4 Revenue Analysis

## Hypotheses Review
1.  **Seasonality**: Is the drop significant?
    - *Method*: T-Test comparing Sep (Pre) vs Oct/Nov (Post).
2.  **Volume vs Price**: Is revenue driven by unit volume?
    - *Method*: Calculate Correlation (Pearson) between Revenue and Units Sold.

## Data Requirements
- **Input Source**: `src/demo_project/input/sales.csv`
- **Columns**: `date`, `revenue`, `units_sold`
- **Validation**:
    - Checked: `sales.csv` exists.
    - Quality: No missing values (assumed for demo).

## Analysis Plan
1.  **EDA**:
    - Plot Daily Revenue Time Series.
    - Distribution of Revenue pre/post Oct 1.
2.  **Hypothesis Tests**:
    - **H1**: T-Test (Sep vs Oct+Nov).
    - **H2**: Correlation Matrix.
