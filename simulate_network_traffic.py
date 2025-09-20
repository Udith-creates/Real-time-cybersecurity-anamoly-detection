import csv
import time
import random
from datetime import datetime

FILE = "network_traffic.csv"

# Initialize CSV with headers
with open(FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "requests"])

while True:
    requests = random.choice([50, 60, 55, 5000, 70, 65, 80, 10000])  # normal and spike values
    log_entry = [datetime.utcnow().isoformat(), requests]
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(log_entry)
    print(f"Added network traffic: {log_entry}")
    time.sleep(3)
