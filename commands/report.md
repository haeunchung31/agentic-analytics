# /report - Interactive Reporting & Synthesis

**Usage**: `/report src/[project_name]/intermediate/analysis_results.md`
**Description**: Synthesize findings into a final Korean report.

## Purpose
Convert technical findings into a business narrative, saved in the project's report directory.

## Workflow Steps

### 1. **Synthesis (Orchestrator)**
- Load analysis results from `src/[project_name]/intermediate/`.
- Synthesize findings relative to `src/[project_name]/intermediate/brainstorm.md`.

### 2. **Interactive Review Loop**
- Focus on "So What?" and business implications.
- Ensure **Korean** language output.

### 3. **Draft Final Report**
- Save final report to `src/[project_name]/report/Final_Report.md` (or `.pdf`/`.pptx` if supported).

## Output Format

```markdown
# [Title in Korean]

## Executive Summary
...
```

## References
- **Input**: `src/[project_name]/intermediate/analysis_results.md`
- **Output**: `src/[project_name]/report/`
- **Skills**: Uses `skills/storytelling.md` for narrative structure.
