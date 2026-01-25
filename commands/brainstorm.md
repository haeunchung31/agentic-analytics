# /brainstorm - Problem Definition & Hypothesis Formation

**Usage**: `/brainstorm [project_name]`
**Description**: Define the business question and hypotheses for an existing project.

## Purpose
Focuses purely on **problem definition**—clarifying "what are we trying to answer?". 
**Pre-requisite**: Project must be initialized via `/initialize [project_name]`.

## Workflow Steps

### 1. **Determine Execution Mode**
Select the mode that matches the user's clarity level:

*   **Mode A (Targeted)**: User has a clear business question.
    *   *Action*: Proceed strictly to Hypothesis Formation.
*   **Mode B (Exploratory)**: User has a fuzzy goal (e.g., "Why is churn up?").
    *   *Action*: Trigger broad EDA first. Do not formulate specific hypotheses yet.
    *   *Output*: Draft a "Research Question" instead of Hypothesis.
*   **Mode C (Ideation)**: User has no idea.
    *   *Action*: Engaged in Socratic Loop. Ask: "What is the key metric?", "What decision is pending?".

### 2. **Gather Context**
- **Messy Phase**: Acknowledge that the first step is often exploring vague questions.
- **Action**: Collect all snippets, notes, stakeholder comments, and background information.
- **Goal**: Move from "Confusion" to "Clarity".

### 2. **Iterative Question Refinement**
- Ask clarifying questions to sharpen the business question:
  - "What decision will this analysis inform?"
  - "What would a successful answer look like?"
- Continue until the question is **specific, measurable, and actionable**.

### 3. **Hypothesis Formation**
- Generate initial hypotheses based on domain knowledge.
- Each hypothesis must be falsifiable and tied to a metric.

### 4. **Output Generation**
- Create structured markdown file: `src/[project_name]/intermediate/brainstorm.md`
- Use `write_to_file` to save.

## Output Format

```markdown
---
type: brainstorm
status: draft
created: YYYY-MM-DD
project: [project_name]
---

# [Descriptive Title]

## Key Question(s)
... 
```

## References
- **Input**: User context / conversation
- **Output**: `src/[project_name]/intermediate/brainstorm.md`
- **Next Step**: `/design src/[project_name]/intermediate/brainstorm.md`
- **Agents**: Invokes `agents/strategist.md` and `agents/orchestrator.md`
- **Skills**: Uses `skills/analysis/kpi.md` for metric definition.
