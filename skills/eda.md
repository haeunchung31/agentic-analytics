---
name: eda
description: "Workflow for Exploratory Data Analysis. Focuses on parallel hypothesis testing and systematic data profiling."
---

# EDA Workflow

**Goal**: Systematically explore data to uncover patterns and relationships using a hypothesis-driven approach.

## Phase 1: Hypothesis Generation
1. **Brainstorm**: Generate 3-5 independent hypotheses based on the business question.
2. **Decompose**: Identify data requirements for each hypothesis.

## Phase 2: Parallel Execution
IF hypotheses are independent, create separate tasks.
- Use `assets/task-template.py`.
- Run using `uv run python tasks/XX_taskname.py`.

## Phase 3: Systematic Profiling (Checklist)
1. **Data Profiling**: Shape, Types, Missingness, Uniqueness.
2. **Univariate**: Histograms, Boxplots, Top N counts.
3. **Bivariate**: Correlations, Groupby Aggregations, Time Series.
4. **Quality Check**: Negative values, Date ranges, Standardization.

## Synthesis
- Combine findings from all streams.
- Identify "So What?" (Actionable Insight).

## References
- **Project Structure**: See `rules/structure.md`.
- **Visualization**: See `rules/visualization.md`.
- **Statistics**: See `rules/statistics.md`.
- **Reporting**: See `skills/reporting.md`.
