import cv2
import time
import numpy as np
from typing import List
from ultralytics import YOLO
from logger import ViolationLogger
from config import YOLO_MODEL, CONF_THRESHOLD, MAX_PERSONS, PERSON_ALERT_COOLDOWN, ALLOWED_CLASSES

class CheatDetector:
    """
    A class for detecting cheating or unauthorized activities in video frames using YOLOv8.
    """
    def __init__(self):
        """
        Initialize the CheatDetector with YOLO model and logger.
        """
        try:
            self.model = YOLO(YOLO_MODEL)
            self.logger = ViolationLogger()
            self.last_person_alert = 0.0
        except Exception as e:
            print(f"Error initializing CheatDetector: {e}")
            raise

    def process(self, frame: np.ndarray) -> np.ndarray:
        """
        Process a video frame for object detection and violation logging.

        Args:
            frame (np.ndarray): Input video frame.

        Returns:
            np.ndarray: Processed frame with annotations.
        """
        try:
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
                        self.logger.log(f"Unauthorized Object Detected: {label}")
                        self.draw_box(
                            frame, x1, y1, x2, y2,
                            f"UNAUTHORIZED: {label}",
                            (0, 0, 255)
                        )

            # 🚨 Multiple Persons Alert
            current_time = time.time()
            if person_count > MAX_PERSONS:
                if current_time - self.last_person_alert > PERSON_ALERT_COOLDOWN:
                    self.logger.log(f"Multiple Persons Detected: {person_count} persons")
                    self.last_person_alert = current_time

                cv2.putText(
                    frame,
                    f"ALERT: {person_count} PERSONS DETECTED",
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
        except Exception as e:
            print(f"Error processing frame: {e}")
            return frame

    def draw_box(self, frame: np.ndarray, x1: int, y1: int, x2: int, y2: int, text: str, color: tuple) -> None:
        """
        Draw a bounding box with label on the frame.

        Args:
            frame (np.ndarray): The frame to draw on.
            x1, y1, x2, y2 (int): Bounding box coordinates.
            text (str): Label text.
            color (tuple): BGR color tuple.
        """
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            frame, text, (x1, y1 - 8),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2
        )
