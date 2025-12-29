import csv
import os
from datetime import datetime

LOG_FILE = "logs/violations.csv"

class ViolationLogger:
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Violation"])

        self.last_violation = None

    def log(self, violation):
        if violation == self.last_violation:
            return  # avoid duplicate spam

        self.last_violation = violation

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), violation])
