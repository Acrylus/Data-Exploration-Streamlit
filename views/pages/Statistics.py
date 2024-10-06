# descriptive_stats.py
import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset from main.py
from Main import load_data

df = load_data()

# Select numeric columns
numeric_cols = df.select_dtypes(include=[np.number])
df[numeric_cols.columns] = df[numeric_cols.columns].fillna(df[numeric_cols.columns].mean())

# Calculate descriptive statistics
descriptive_stats = {}
for col in numeric_cols.columns:
    stats_result = stats.describe(numeric_cols[col].dropna())
    descriptive_stats[col] = {
        'Number of Observations': stats_result.nobs,
        'Min': stats_result.minmax[0],
        'Max': stats_result.minmax[1],
        'Mean': stats_result.mean,
        'Variance': stats_result.variance,
        'Skewness': stats_result.skewness,
        'Kurtosis': stats_result.kurtosis,
    }

stats_summary = pd.DataFrame(descriptive_stats).T

# Additional metrics (Median, Mode, Percentiles)
for col in numeric_cols.columns:
    stats_summary.loc[col, 'Median'] = numeric_cols[col].median()
    stats_summary.loc[col, 'Mode'] = numeric_cols[col].mode().iloc[0]
    stats_summary.loc[col, '25th Percentile'] = numeric_cols[col].quantile(0.25)
    stats_summary.loc[col, '50th Percentile'] = numeric_cols[col].quantile(0.5)
    stats_summary.loc[col, '75th Percentile'] = numeric_cols[col].quantile(0.75)

# Display Descriptive Statistics
st.write("Descriptive Statistics Summary:")
st.dataframe(stats_summary)
