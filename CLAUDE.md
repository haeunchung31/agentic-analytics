# CLAUDE.md - Agentic Analytics

## Project Overview
This repository functions as an agentic system for Data Analytics and Modeling.
Focus: **Business Modeling, Financial Analysis, and Hypothesis Testing**.

## Commands
- **`/plan`**: [Plan Analysis](commands/plan.md) - Generate detailed hypothesis and test plan.
- **`/eda`**: [Run EDA](skills/eda.md) - Execute standard exploratory data profiling.
- **`/report`**: [Generate Report](skills/reporting.md) - Synthesize findings into executive summary.

## Rules
- **Business Focus**: Always tie analysis back to the business question.
- **Financial Rigor**: Use correct financial terminologies. See [Statistics](rules/statistics.md).
- **Data Safety**: READ-ONLY SQL. No PII. See [Privacy](rules/privacy.md).
- **Aesthetics**: See [Visualization](rules/visualization.md).
- **Structure**: See [Project Structure](rules/structure.md).

## Agents
- **Hypothesis Agent**: Strategist.
- **SQL Agent**: Impala expert, efficient querying.
- **DS Agent**: Stats/ML + dbt modeling.
- **Review Agent**: Product Owner persona.

## Project Standards

### Python Environment
This project uses `uv` for Python package management. **Always use `uv run` for script execution:**

```bash
# Run Python scripts
uv run python src/script.py
uv run python script.py --arg1 value1

# Manage packages
uv add package-name --dev
uv sync  # Install dependencies from lock file
```

**Never use:** `python`, `python3`, or `pip` directly.

### Virtual Environment
```bash
# Activate environment manually if needed
source .venv/bin/activate
```

### Code Style Requirements
1. **Interactive Scripts:** Use `# %%` cell markers for section separation.
2. **Variable Naming:** Descriptive names (`stats_df`, `robust_importance`).
3. **Visualization:** Sort by effect size, use violin/box plots for non-normal data.
4. **Documentation:** Korean for reports, English for code/comments.
