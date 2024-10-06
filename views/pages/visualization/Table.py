# # correlation_matrix.py
# import streamlit as st
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from Main import load_data  # Adjust the import according to your project structure

# # Load the dataset
# df = load_data()

# # Select numeric columns
# numeric_cols = df.select_dtypes(include=[np.number])

# # Correlation Matrix
# st.write("### Correlation Matrix of Numeric Features")
# correlation_matrix = numeric_cols.corr()

# fig, ax = plt.subplots(figsize=(12, 8))
# sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True, cbar_kws={"shrink": .8}, ax=ax)
# ax.set_title('Correlation Matrix of Numeric Features')
# st.write(fig)
