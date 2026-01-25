# Visualization Standards

**Owner**: Data Scientist & Orchestrator
**Purpose**: Ensure all visual outputs are "Premium", clean, and self-explanatory.

## 1. Critical Standards (Must Follow)
- **Financial Specifics**:
    - **Units**: Never use scientific notation. Use **조/억/만** for large currency amounts.
    - **Fonts**: Must configure Korean fonts first.
- **Anti-Patterns**:
    - ❌ **Scientific Notation**: Never use it.
    - ❌ **Bar Charts with Error Bars**: Avoid for non-normal financial data. Use Violin/Box plots.
    - ❌ **Pie Charts**: Generally avoid.
    - ❌ **3D Charts**: Never use.

## 2. General Principles
- **Less is More**: Remove "chart junk" (excessive gridlines, borders, background colors).
- **Direct Labeling**: Avoid legends if possible. Label lines/bars directly.
- **Title as Headline**: The title should state the insight (e.g., "Conversion dropped 15% in May") not the metric (e.g., "Monthly Conversion Rate").

## 2. Color Palettes
- **Primary**: Use brand colors or high-contrast, professional accessible palettes (e.g., Okabe-Ito).
- **Semantic Colors**:
    - **Positive/Growth**: Green / Blue (context dependent).
    - **Negative/Decline**: Red / Orange.
    - **Neutral**: Grey (for context or benchmarks).
- **Keep it Simple**: Max 3-4 distinct colors per chart.

## 3. Chart Types & Best Practices
### Comparison
- **Bar Chart**: For categorical comparison. Sort bars by value (unless ordinal).
- **Lollipop Chart**: A cleaner alternative to bar charts for many categories.

### Trend
- **Line Chart**: For time series. Use thick lines (2.5pt+).
- **Area Chart**: For volume over time.

### Distribution
- **Histogram**: For continuous distribution.
- **Box Plot**: For summary of distribution (Median, IQR, Outliers).

### Relationship
- **Scatter Plot**: Reduce opacity (alpha) to manage overplotting.
- **Bubble Chart**: Scatter plot + Size dimension.

## 4. Annotations
**Rule**: Every major insight must be annotated.
- **Peaks/Troughs**: "All-time high reached on Black Friday."
- **Events**: "Marketing campaign launched here."
- **Thresholds**: "Target: 20%" (Reference line).
