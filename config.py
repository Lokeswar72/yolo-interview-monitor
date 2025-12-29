# YOLO Model Configuration
YOLO_MODEL = "yolov8n.pt"

# Detection Settings
CONF_THRESHOLD = 0.5  # Confidence threshold for detections
FRAME_SKIP = 2        # Process every Nth frame for performance

# Proctoring Rules
ALLOWED_CLASSES = ["person"]  # List of allowed object classes
MAX_PERSONS = 1               # Maximum allowed persons in frame

# Alert Settings
PERSON_ALERT_COOLDOWN = 3.0   # Seconds between repeated person alerts
ENABLE_LOGGING = True         # Enable violation logging to CSV
