import csv
import time
import random
from datetime import datetime

FILE = "file_transfers.csv"
USERS = ["user1", "user2", "user3"]

# Initialize CSV with headers
with open(FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "username", "volume_mb"])

while True:
    username = random.choice(USERS)
    volume = random.choice([20, 25, 18, 2000, 22, 19, 2100])  # normal and exfiltration values
    log_entry = [datetime.utcnow().isoformat(), username, volume]
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(log_entry)
    print(f"Added file transfer: {log_entry}")
    time.sleep(3)
