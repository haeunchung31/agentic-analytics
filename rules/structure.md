# Project Structure & Naming

## Directory Layout
Standard structure for all analytics projects:

```
src/[project-id]/
├── input/              # CSV data files (Read-Only)
├── output/             # Visualizations and result CSVs
├── tasks/              # Parallel task scripts
└── report/             # Markdown reports (only when requested)
```

## File Naming
- **Scripts**: `snake_case.py` (e.g., `churn_analysis.py`).
- **Parallel Tasks**: `XX_description.py` (e.g., `01_distribution.py`).
- **Data**: `snake_case.csv`.
- **Images**: `snake_case.png` (include variable name if possible).

## Script Standards
- **Interactive**: Always use `# %%` for cells.
- **Output**: Save artifacts to `output/`.
