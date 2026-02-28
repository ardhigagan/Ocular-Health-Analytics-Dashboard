import pandas as pd
import numpy as np

# 1. Load the dataset
file_path = 'Dataset/glaucoma_dataset.csv'
df = pd.read_csv(file_path)

# 2. Universal Name Cleaning (Keeps the table looking professional)
df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

# Rename the long IOP column for easier use in your Dashboard
if 'intraocular_pressure_(iop)' in df.columns:
    df.rename(columns={'intraocular_pressure_(iop)': 'iop'}, inplace=True)

# 3. Remove Duplicates
initial_count = len(df)
df.drop_duplicates(inplace=True)
print(f"Removed {initial_count - len(df)} duplicate records.")

# 4. Delete Rows with ANY Empty Cells
rows_before = len(df)
df.dropna(inplace=True)
print(f"Deleted {rows_before - len(df)} rows containing null values.")

# 5. Feature Engineering 
if 'vertical_cdr' in df.columns and 'horizontal_cdr' in df.columns:
    df['mean_cdr'] = df[['vertical_cdr', 'horizontal_cdr']].mean(axis=1)

# Add age groups for the Risk Heatmap
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '81+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

# 6. Export the Full, Polished Dataset
df.to_csv('cleaned_ocular_health_data.csv', index=False)

print("Success! Cleaned table saved as 'cleaned_ocular_health_data.csv'.")
