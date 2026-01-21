# Visualization Standards

**Goal**: Create "Rich", "Premium", and "Actionable" visualizations.

## Principles
1. **Less is More**: Remove chart junk (borders, excessive gridlines).
2. **Color Strategy**:
   - Use **Semantic Colors** (Green = Good, Red = Bad) only when meaning is clear.
   - Use **Harmonious Palettes** (e.g., Blues, Teals, Purples) for categorical data.
   - **Dark Mode** preference for screen-based reports.
3. **Typography**: Use clean, sans-serif fonts (Roboto, Inter).

## Financial Specifics
- **Units**: Never use scientific notation. Use **조/억/만** for large currency amounts.
- **Fonts**: Must configure Korean fonts first.
- **Layout**: Place legends outside plot. Save as PNG with `dpi=150, bbox_inches='tight'`.

## Chart Selection
- **Comparison**: Bar Chart (Horizontal for long labels).
- **Trend**: Line Chart (smooth lines).
- **Distribution**: Histogram or KDE.
- **Composition**: Stacked Bar (Avoid Pie Charts unless < 3 categories).
- **Relationship**: Scatter Plot.

## Anti-Patterns
- ❌ **Scientific Notation**: Never use it.
- ❌ **Bar Charts with Error Bars**: Avoid for non-normal financial data. Use Violin/Box plots.
- ❌ **Pie Charts**: Generally avoid.
- ❌ **3D Charts**: Never use.

## Python Implementation
```python
import seaborn as sns
import matplotlib.pyplot as plt

def set_style():
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.set_context("talk")
    # Custom palette & Params...
```
