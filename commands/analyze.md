# /analyze - Analysis Execution

**Usage**: `/analyze src/[project_name]/intermediate/design.md`
**Description**: Execute the technical plan.

## Purpose
Run the analysis using scripts within the project directory.

## Workflow Steps

### 1. **Load Design Context**
- Read `src/[project_name]/intermediate/design.md`.
- Determine paths for input (`src/[project_name]/input/`) and output (`src/[project_name]/output/`).

### 2. **Exploratory Data Analysis (Mandatory)**
- **Rule**: You MUST run EDA before Hypothesis Testing.
- **Action**: Execute checks from `skills/analysis/eda.md`.
- **Output**: Save summary to `src/[project_name]/intermediate/eda_overview.md`.

### 3. **Hypothesis Testing Execution**
- **Action**: Iterate through **ALL** hypotheses defined in `design.md`.
- Write analysis scripts (e.g., `src/[project_name]/02_analysis.py`) to test them in a single batch.
- Save plots to `src/[project_name]/output/figures/`.
- Save results to `src/[project_name]/output/results.json`.

### 4. **Output Results**
- Generate `src/[project_name]/intermediate/analysis_results.md`.

## Output Format

```markdown
---
type: analysis
status: complete
project: [project_name]
---

# Analysis Results

## Artifacts
- **Code**: `src/[project_name]/*.py`
- **Data**: `src/[project_name]/output/...`
...
```

## References
- **Input**: `src/[project_name]/intermediate/design.md`
- **Output**: `src/[project_name]/intermediate/analysis_results.md`
- **Next Step**: `/report src/[project_name]/intermediate/analysis_results.md`
