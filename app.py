from flask import Flask, render_template, Response
import logging
from camera import VideoCamera

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

try:
    camera = VideoCamera()
    logging.info("Camera initialized successfully")
except Exception as e:
    logging.error(f"Failed to initialize camera: {e}")
    camera = None

@app.route("/")
def index():
    """
    Render the main page.
    """
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    """
    Stream the video feed.
    """
    if camera is None:
        return "Camera not available", 500
    return Response(
        camera.stream(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    logging.info("Starting Flask app...")
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
