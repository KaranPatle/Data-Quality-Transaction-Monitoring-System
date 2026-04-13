import pandas as pd
import numpy as np
from faker import Faker
import random

# Reproducibility
random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

num_rows = 10000

cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]
categories = ["Electronics", "Fashion", "Groceries"]
payments = ["UPI", "Card", "Cash"]

data = []

for i in range(num_rows):
    # Generate base amount
    amount = round(random.uniform(100, 5000), 2)

    # Introduce bad data safely
    if random.random() < 0.02:
        amount = None  # missing
    elif random.random() < 0.01 and amount is not None:
        amount = -amount  # negative only if valid

    row = {
        "Transaction_ID": i + 1,
        "Customer_ID": random.randint(100, 500),
        "Transaction_Date": fake.date_between(start_date="-6M", end_date="today"),
        "Amount": amount,
        "City": random.choice(cities),
        "Product_Category": random.choice(categories),
        "Payment_Method": random.choice(payments)
    }

    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Convert date column properly
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

# Add duplicates (controlled)
duplicates = df.sample(50, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save
df.to_csv("transactions.csv", index=False)

print("Dataset generated successfully!")
print(f"Total rows: {len(df)}")
print(f"Missing Amounts: {df['Amount'].isnull().sum()}")
print(f"Negative Amounts: {(df['Amount'] < 0).sum()}")