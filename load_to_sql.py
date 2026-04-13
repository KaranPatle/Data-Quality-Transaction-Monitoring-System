import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv('data/transactions.csv')

# Create DB
conn = sqlite3.connect('data/transactions.db')

# Store table
df.to_sql('transactions', conn, if_exists='replace', index=False)

print("✅ Data loaded into SQL database")