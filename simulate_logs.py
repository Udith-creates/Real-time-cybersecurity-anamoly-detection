import csv
import time
import random
from datetime import datetime

FILE = "log.csv"
USERS = ["user1", "user2", "user3"]
LOCATIONS = ["Delhi", "Mumbai", "Russia", "London", "New York"]
ACTIONS = ["login", "file_access", "logout"]

# Initialize CSV with headers
with open(FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "username", "location", "action"])

while True:
    log_entry = [
        datetime.utcnow().isoformat(),
        random.choice(USERS),
        random.choice(LOCATIONS),
        random.choice(ACTIONS),
    ]
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(log_entry)
    print(f"Added log: {log_entry}")
    time.sleep(3)
