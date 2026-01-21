# /eda - Exploratory Data Analysis

**Usage**: `/eda [Dataset/Table]`
**Description**: systematic profiling and exploration of a dataset.

## Workflow steps
1. **Load Skills**: Read `skills/eda_framework.md` to ensure standard checks are run.
2. **Execute Profiling**:
   - Run simple SQL `SELECT` counts, null checks, and distinct counts.
   - **Crucial**: DO NOT extract millions of rows. Use `LIMIT 1000` or aggregate logic.

3. **Visual Exploration**:
   - Use `skills/visualization.md` standards.
   - Create 3-5 core plots:
     - Histogram of key metric.
     - Trend over time.
     - Scatter plot if correlation suspected.

4. **Output**:
   - A brief summary of data quality and distribution.
   - Flag any "weirdness" (e.g., 90% nulls in a critical column).
