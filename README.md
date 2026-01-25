# Oh My Analytics: Agentic Data Workflow

A structured, agent-driven framework for turning vague business questions into actionable, high-quality insights.

## Core Workflow

This repository operates on a strict **Project-Based Workflow** controlled by slash commands.

### 1. Initialize (`/initialize`)
**Command**: `/initialize [project_name]`
- **Action**: Creates the standard directory skeleton at `src/[project_name]/`.
- **Created Folders**: `input/`, `output/`, `intermediate/`, `report/`, `sql/`.

### 2. Brainstorm (`/brainstorm`)
**Command**: `/brainstorm [project_name]`
- **Goal**: Define the *real* business problem.
- **Modes**: Targeted (Hypothesis), Exploratory (EDA first), or Ideation (Socratic).
- **Agents**: Strategist + Orchestrator.
- **Output**: `src/[project_name]/intermediate/brainstorm.md`.

### 3. Design (`/design`)
**Command**: `/design src/[project_name]/intermediate/brainstorm.md`
- **Goal**: Create a technical plan and validate data availability.
- **Agents**: Data Scientist + Data Engineer.
- **Output**: `src/[project_name]/intermediate/design.md`.

### 4. Analyze (`/analyze`)
**Command**: `/analyze src/[project_name]/intermediate/design.md`
- **Goal**: Execute reproducible Python analysis for **all** planned hypotheses (batch execution).
- **Rules**: **Mandatory EDA** before Hypothesis Testing.
- **Agents**: Data Scientist.
- **Output**: `eda_overview.md`, Scripts (`*.py`), and Results (`output/`).

### 5. Report (`/report`)
**Command**: `/report src/[project_name]/intermediate/analysis_results.md`
- **Goal**: Synthesize findings into a final **Korean** report.
- **Agents**: Orchestrator.
- **Output**: Final report in `src/[project_name]/report/`.

---

## Repository Structure

```
.
├── agents/             # Agent Personas (Orchestrator, Strategist, DS, DE)
├── commands/           # Slash command definitions (The Workflow Engine)
├── knowledge_base/     # Business context and Schema definitions
├── rules/              # Global constraints (Privacy, Structure)
├── skills/             # Modular Capabilities (Statistics, Strategy, Viz, etc.)
└── src/                # Project Workspace (Where the work happens)
    └── [project_name]/ # Isolated project instances
```

## Agents
- **Orchestrator**: Project Lead. Ensures "So What?" and business alignment.
- **Strategist**: Business Analyst. Frames problems and hypotheses.
- **Data Scientist (DS)**: The Builder. Writes Code, models data, visualizes.
- **Data Engineer (DE)**: The Provider. Fetches and validates data (SQL).

## Getting Started
1. **Initialize**: `/initialize churn_analysis_q1`
2. **Define**: `/brainstorm churn_analysis_q1` -> "Why is churn up?"
3. **Plan**: `/design src/churn_analysis_q1/intermediate/brainstorm.md`
4. **Execute**: `/analyze src/churn_analysis_q1/intermediate/design.md`
5. **Deliver**: `/report src/churn_analysis_q1/intermediate/analysis_results.md`
