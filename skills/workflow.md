---
name: analytical-workflow
description: "Standard End-to-End Analytical Workflow. From Request to Final Insight."
---

# Analytical Workflow

**Goal**: Transform a vague business question into a concrete, actionable insight using a structured approach.

## Phase -1: Initialization (`/initialize [project_name]`)
1. **Setup**: Create standard directory layout (`src/[project_name]/{input,output,intermediate...}`).

## Phase 0: Problem Brainstorming (`/brainstorm [project_name]`)
1. **Clarify Intent**: Identify the *real* business question and "So What?".
2. **Context Gathering**: Collect all background info and stakeholders.
3. **Hypothesis Generation**: Formulate testable, metrics-linked hypotheses.
4. **Intermediate Hub**: Store brainstorm in `src/[project_name]/intermediate/`.

## Phase 1: Technical Design (`/design`)
1. **Methodology Selection**: Match statistical tests/models to hypotheses.
2. **Data Assessment**: Identify required tables and columns.
3. **DuckDB Validation**: Validate the "Ideal Dataset" structure actually works.
4. **Technical Plan**: Draft SQL skeletons and analysis script outlines.
5. **Output**: Save to `src/[project_name]/intermediate/design.md`.

## Phase 2: Execution & Analysis (`/analyze`)
1. **Reproducible Scripts**: Create Python scripts in `src/[project_name]/` (e.g., `01_data_prep.py`).
2. **Data Profiling**: Run quality checks on `src/[project_name]/input/` data.
3. **Hypothesis Testing**: Execute statistical tests and save results to `src/[project_name]/output/`.
4. **Artifacts**: Save figures to `output/figures/` and metrics to `output/results.json`.

## Phase 3: Synthesis & Reporting (`/report`)
1. **Orchestrator Review**: Review findings against original brainstorm goals.
2. **Interpretation**: Focus on the "So What?" (Business implications).
3. **Interactive Polish**: Review draft summaries with the user.
4. **Korean Output**: Deliver final report to `src/[project_name]/report/`.

## References
- **Statistics**: See `skills/statistics.md`.
- **Strategy**: See `skills/strategy.md`.
- **Storytelling**: See `skills/storytelling.md`.
- **EDA**: See `skills/analysis/eda.md`.
- **Structure**: See `rules/structure.md`.
