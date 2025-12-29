import cv2
import numpy as np
from typing import Generator
from detector import CheatDetector
from config import FRAME_SKIP

class VideoCamera:
    """
    Handles video capture from webcam and processes frames with CheatDetector.
    """
    def __init__(self):
        """
        Initialize the camera and detector.
        """
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                raise ValueError("Unable to access webcam")
            self.detector = CheatDetector()
            self.frame_count = 0
        except Exception as e:
            print(f"Error initializing VideoCamera: {e}")
            raise

    def __del__(self):
        """
        Release the camera when object is destroyed.
        """
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()

    def stream(self) -> Generator[bytes, None, None]:
        """
        Generate a stream of processed video frames.

        Yields:
            bytes: JPEG encoded frame with MJPEG boundary.
        """
        try:
            while True:
                success, frame = self.cap.read()
                if not success:
                    print("Failed to read frame from camera")
                    break

                self.frame_count += 1

                # Skip frames for performance
                if self.frame_count % FRAME_SKIP == 0:
                    frame = self.detector.process(frame)

                _, buffer = cv2.imencode(".jpg", frame)
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" +
                    buffer.tobytes() + b"\r\n"
                )
        except Exception as e:
            print(f"Error in video stream: {e}")
        finally:
            self.cap.release()
