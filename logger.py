import csv
import os
from datetime import datetime
from config import ENABLE_LOGGING

LOG_FILE = "logs/violations.csv"

class ViolationLogger:
    """
    Logger for recording violations to a CSV file.
    """
    def __init__(self):
        if not ENABLE_LOGGING:
            return
        os.makedirs("logs", exist_ok=True)
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Violation"])

        self.last_violation = None

    def log(self, violation: str) -> None:
        """
        Log a violation if logging is enabled.

        Args:
            violation (str): Description of the violation.
        """
        if not ENABLE_LOGGING:
            return

        if violation == self.last_violation:
            return  # Avoid duplicate spam

        self.last_violation = violation

        try:
            with open(LOG_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), violation])
        except Exception as e:
            print(f"Error logging violation: {e}")
