import pandas as pd
from datetime import datetime

# Load data
df = pd.read_csv('data/transactions.csv')

issues = []

# 1. Missing values check
missing = df.isnull().sum()
for col in missing.index:
    if missing[col] > 0:
        issues.append({
            "Issue_Type": "Missing Values",
            "Column": col,
            "Count": missing[col],
            "Timestamp": datetime.now()
        })

# 2. Duplicate rows check
duplicates = df.duplicated().sum()
if duplicates > 0:
    issues.append({
        "Issue_Type": "Duplicate Rows",
        "Column": "All",
        "Count": duplicates,
        "Timestamp": datetime.now()
    })

# 3. Negative transaction check
if 'Amount' in df.columns:
    negative = (df['Amount'] < 0).sum()
    if negative > 0:
        issues.append({
            "Issue_Type": "Negative Values",
            "Column": "Amount",
            "Count": negative,
            "Timestamp": datetime.now()
        })

# 4. Outlier detection (simple)
if 'Amount' in df.columns:
    mean = df['Amount'].mean()
    std = df['Amount'].std()
    outliers = df[(df['Amount'] > mean + 3*std) | (df['Amount'] < mean - 3*std)]

    if len(outliers) > 0:
        issues.append({
            "Issue_Type": "Outliers",
            "Column": "Amount",
            "Count": len(outliers),
            "Timestamp": datetime.now()
        })

# Convert to DataFrame
issues_df = pd.DataFrame(issues)

# Save report
issues_df.to_csv('output/incident_report.csv', index=False)

print("✅ Data Quality Check Completed")
print(issues_df)