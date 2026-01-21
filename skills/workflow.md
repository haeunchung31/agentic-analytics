---
name: analytical-workflow
description: "Standard End-to-End Analytical Workflow. From Request to Final Insight."
---

# Analytical Workflow

**Goal**: Transform a vague business question into a concrete, actionable insight using a structured approach.

## Phase 0: Orchestration & Planning (Orchestrator + Strategist)
1. **Clarify Intent**: "What is the *real* business question?" (Why do they want to know this?)
2. **Defined Success**: What does the output look like? (Dashboard, slide deck, One-pager?)
3. **Hypothesis Generation**: Formulate testable hypotheses (e.g., "Conversion dropped because of payment gateway latency").

## Phase 1: Data Acquisition (Data Engineer)
1. **Schema Check**: Verify table availability and freshness.
2. **Query Construction**: Write efficient SQL.
3. **Extraction**: Pull data to local/staging environment.

## Phase 2: Analysis & Modeling (Data Scientist)
1. **EDA & Profiling**: Check data quality, distributions, and outliers.
2. **Hypothesis Testing**: Run statistical tests (T-test, Chi-square).
3. **Modeling**: Apply predictive models if needed (Regression, Forecasting).

## Phase 3: Synthesis (Orchestrator)
1. **Interpretation**: Interpret the results in business terms.
2. **"So What?"**: What should the business DO with this information?
3. **Review**: Check against "Rich Aesthetics" and business alignment.

## References
- **Methodology**: See `skills/methodology.md`.
- **Reporting**: See `skills/reporting.md`.
