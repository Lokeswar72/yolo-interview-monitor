YOLO_MODEL = "yolov8n.pt"

# Detection confidence
CONF_THRESHOLD = 0.5

# Performance optimization
FRAME_SKIP = 2   # process every Nth frame

# Proctoring rules
ALLOWED_CLASSES = ["person"]   # ONLY allowed object
MAX_PERSONS = 1                # more than this = alert

# Alert control
PERSON_ALERT_COOLDOWN = 3      # seconds
