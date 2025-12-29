import cv2
import time
from ultralytics import YOLO
from logger import ViolationLogger
from config import YOLO_MODEL, CONF_THRESHOLD, MAX_PERSONS, PERSON_ALERT_COOLDOWN, ALLOWED_CLASSES

class CheatDetector:
    def __init__(self):
        self.model = YOLO(YOLO_MODEL)
        self.logger = ViolationLogger()
        self.last_person_alert = 0

    def process(self, frame):
        results = self.model(frame, conf=CONF_THRESHOLD, verbose=False)
        person_count = 0

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                if label in ALLOWED_CLASSES:
                    if label == "person":
                        person_count += 1
                        self.draw_box(frame, x1, y1, x2, y2, "Person", (0, 255, 0))
                else:
                    # Unauthorized object
                    self.logger.log("Unauthorized Object Detected")
                    self.draw_box(
                        frame, x1, y1, x2, y2,
                        f"UNAUTHORIZED: {label}",
                        (0, 0, 255)
                    )

        # 🚨 Multiple Persons Alert
        current_time = time.time()
        if person_count > MAX_PERSONS:
            if current_time - self.last_person_alert > PERSON_ALERT_COOLDOWN:
                self.logger.log("Multiple Persons Detected")
                self.last_person_alert = current_time

            cv2.putText(
                frame,
                "ALERT: MULTIPLE PERSONS DETECTED",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

        # Display count
        cv2.putText(
            frame,
            f"Persons in frame: {person_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        return frame

    def draw_box(self, frame, x1, y1, x2, y2, text, color):
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            frame, text, (x1, y1 - 8),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2
        )
