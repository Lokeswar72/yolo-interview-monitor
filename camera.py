import cv2
from detector import CheatDetector
from config import FRAME_SKIP

class VideoCamera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = CheatDetector()
        self.frame_count = 0

    def stream(self):
        while True:
            success, frame = self.cap.read()
            if not success:
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
