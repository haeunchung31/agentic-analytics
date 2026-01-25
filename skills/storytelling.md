# Storytelling & Reporting

**Owner**: Orchestrator / Senior Data Scientist
**Purpose**: Construct a compelling narrative and deliver the final output.

> [!CAUTION]
> **Critical Language Rule**: All reasoning, prompting, and intermediate artifacts (`.md` files) are in **English**. The **FINAL REPORT** delivered to stakeholders must be in **KOREAN (한국어)**.

## 1. Core Principles
-   **Headline Driven**: Every section/slide must have a clear takeaway message (e.g., "Churn increased by 15% due to pricing change").
-   **So What?**: Always explain the business implication, not just the number.
-   **Visuals First**: Narrative should support the visuals.

## 2. Story Frameworks

### Framework 1: The Problem-Solution Story
1.  **The Hook**: "We're losing $2.4M annually to preventable churn."
2.  **The Context**: Current churn rate vs. industry avg.
3.  **The Problem**: Pattern analysis (e.g., failed onboarding).
4.  **The Insight**: "Customers who don't engage in first 14 days are 4x likely to churn."
5.  **The Solution**: Specific recommendation (e.g., New onboarding flow).
6.  **Expected Impact**: ROI projection.

### Framework 2: The Trend Story (Before/After)
1.  **Where We Started**: "Q3 ended below target."
2.  **What Changed**: "We launched feature X in October."
3.  **The Transformation**: Data comparison (Q3 vs Q4).
4.  **Key Insight**: "Feature X drove 30% increase in retrieval."

### Framework 3: The Comparison Story (Trade-offs)
1.  **The Question**: "Should we expand to EMEA or APAC?"
2.  **Metric Comparison**: Side-by-side scoring (Market Size, Growth, Competition).
3.  **The Recommendation**: "APAC first. Higher growth, less competition."
4.  **Risk Mitigation**: Address potential downsides.

## 3. Visualization Techniques
-   **Progressive Reveal**: Start simple (one line), then layer complexity (add benchmarks, then segments).
-   **Contrast & Compare**: Use side-by-side charts to highlight differences (Before/After, Segment A vs B).
-   **Annotation**: **ALWAYS** annotate key peaks, troughs, and events directly on the chart. Don't make the user hunt for meaning.

## 4. Report Structure (The "Paper")
1.  **Executive Summary** (The "BLUF" - Bottom Line Up Front)
    -   **Context**: The Question.
    -   **Key Insight**: The Answer.
    -   **Recommendation**: The Action.
2.  **Detailed Findings**
    -   Logical flow (A led to B).
    -   Supporting charts (See `skills/visualization.md`).
3.  **Appendices**
    -   Methodology, specific query logic.

## 5. Writing Best Practices
-   **Headlines**: Use active voice. "Revenue grew" -> "New pricing strategy drove 15% revenue growth".
-   **Uncertainty**: Be honest. "With 95% confidence...", "Sample size n=500".
-   **Transition**: Use phrases like "This leads us to ask...", "The data reveals...", "Consequently...".

