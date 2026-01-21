# /report - Final Report Generation

**Usage**: `/report`
**Description**: Synthesizes findings into a business-ready document.

## Workflow steps
1. **Aggregate Findings**:
   - Review all analysis outputs, charts, and notes from this session.

2. **Invoke Review Agent**:
   - Check against `agents/review_agent.md`.
   - Ask: "Does this answer the *original* business question?"

3. **Draft Report**:
   - Follow individual section guidelines in `skills/reporting.md`.
   - **Executive Summary**: Must be top-loaded.
   - **Visuals**: Embed best charts.

4. **Final Polish**:
   - Ensure no PII is included (`rules/data_privacy.md`).
   - Check tone (Professional, Financial).
