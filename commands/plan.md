# /plan - Hypothesis & Experiment Design

**Usage**: `/plan [Business Question]`
**Description**: Initiates the strategic planning phase for an analysis.

## Workflow steps
1. **Invoke Hypothesis Agent**:
   - Deconstruct the `[Business Question]` using a financial framework (e.g., Issue Tree).
   - Generate testable hypotheses.
   - Output a list of required data.

2. **Invoke SQL Agent (Conditional)**:
   - **Trigger**: Only invoke if the user explicitly prompts for SQL generation or data extraction.
   - **Action**:
     - Identify which tables in `knowledge_base/schema_context.md` contain the required data.
     - Draft *skeleton* queries (checking for feasibility).

3. **Output**:
   - A `plan.md` file in the current working directory outlining the approach.
   - Use `write_to_file` to save this plan.

## Example
User: "/plan Why did our LTV drop in Q3?"
Agent: "Analyzing LTV components (AOV, Purchase Frequency)...
Hypothesis 1: AOV dropped due to summer sale discount (Requires: `transactions` table).
Hypothesis 2: Churn increased in high-value segment (Requires: `user_retention` table)...
(SQL Agent NOT invoked as not requested)"

User: "/plan Check feasibility of extracting daily active users for last year using SQL"
Agent: "Hypothesis: DAU trend analysis...
Invoking SQL Agent to check schema...
Drafting query for `daily_active_users` table..."
