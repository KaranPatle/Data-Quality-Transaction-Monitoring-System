import os
from datetime import datetime

file_path = "data/transactions.csv"

file_time = datetime.fromtimestamp(os.path.getmtime(file_path)).time()

expected_time = datetime.strptime("10:00", "%H:%M").time()

if file_time > expected_time:
    print("❌ SLA BREACH: Data arrived late")
else:
    print("✅ SLA OK: Data arrived on time")