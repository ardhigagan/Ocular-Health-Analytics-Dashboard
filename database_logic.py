import sqlite3
import pandas as pd

# Load your cleaned data
df = pd.read_csv('cleaned_ocular_health_data.csv')

# Connect to SQLite (it creates the file if it doesn't exist)
conn = sqlite3.connect('ocular_health.db')

# Write the SQL 'Create Table' and 'Insert' logic in one go
df.to_sql('OcularAnalytics', conn, if_exists='replace', index=False)

print("Database created successfully!")
conn.close()