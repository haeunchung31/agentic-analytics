
import pandas as pd
from scipy import stats
import json
import os

# Set paths
base_dir = "src/demo_project"
input_path = f"{base_dir}/input/sales.csv"
output_dir = f"{base_dir}/output"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(f"{output_dir}/figures", exist_ok=True)

# 1. Load Data
print(f"Loading data from {input_path}...")
df = pd.read_csv(input_path)
df['date'] = pd.to_datetime(df['date'])
print("Data Loaded. Head:")
print(df.head())

# 2. EDA
print("\n--- EDA ---")
print(df.describe())

# 3. Hypothesis Testing
results = {}

# H1: Seasonality (Sep vs Oct+Nov)
# Split data
sep_data = df[df['date'].dt.month == 9]['revenue']
oct_nov_data = df[df['date'].dt.month.isin([10, 11])]['revenue']

print("\n--- Hypothesis 1: Seasonality ---")
print(f"Mean Revenue (Sep): {sep_data.mean():.2f}")
print(f"Mean Revenue (Oct+Nov): {oct_nov_data.mean():.2f}")

t_stat, p_val = stats.ttest_ind(sep_data, oct_nov_data, equal_var=False)
print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_val:.4f}")
results['h1_seasonality'] = {
    'mean_sep': sep_data.mean(),
    'mean_oct_nov': oct_nov_data.mean(),
    'p_value': p_val,
    'significant': bool(p_val < 0.05)
}

# H2: Volume vs Price
print("\n--- Hypothesis 2: Volume vs Price ---")
corr = df['revenue'].corr(df['units_sold'])
print(f"Correlation (Revenue vs Units): {corr:.4f}")
results['h2_correlation'] = {
    'correlation': corr
}

# Save Results
with open(f"{output_dir}/results.json", "w") as f:
    json.dump(results, f, indent=4)
print(f"\nResults saved to {output_dir}/results.json")
