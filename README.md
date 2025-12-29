# YOLO Interview Monitor 🕵️‍♂️

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A real-time AI-based proctoring system designed to monitor interviews or exams using computer vision. It utilizes the YOLOv8 model to detect unauthorized objects and ensure only one person is present in the frame. 🚀

## 🚀 Features

- **Real-time Monitoring**: Streams video from the webcam via a Flask web interface. 📹
- **Person Detection**: Alerts if more than one person is detected in the frame (`MAX_PERSONS` rule). 👥
- **Unauthorized Object Detection**: Identifies and logs objects that are not in the allowed list (e.g., cell phones, if not allowed). 🚫📱
- **Violation Logging**: Automatically records violations with timestamps to a CSV file (`logs/violations.csv`). 📝
- **Performance Optimization**: Includes frame skipping to maintain smooth playback on lower-end hardware. ⚡

## 📋 Prerequisites

- Python 3.8 or higher 🐍
- A working webcam 📷

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yolo_interview_monitor.git
   cd yolo_interview_monitor
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   *Note: The `ultralytics` package will automatically download the `yolov8n.pt` model on the first run if it is not present.* 📥

## 🎯 Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   `http://127.0.0.1:5000` 🌐

3. The system will start monitoring. Violations will be highlighted on the video feed and logged to the `logs/` directory. ⚠️

## ⚙️ Configuration

You can customize the behavior in `config.py`:

- **`ALLOWED_CLASSES`**: List of objects allowed in the frame (default: `["person"]`). ✅
- **`MAX_PERSONS`**: Maximum number of people allowed (default: `1`). 👤
- **`CONF_THRESHOLD`**: Confidence threshold for detections (default: `0.5`). 🎯
- **`PERSON_ALERT_COOLDOWN`**: Time in seconds between repeated alerts for multiple persons. ⏱️

## 📁 Project Structure

```
yolo_interview_monitor/
├── app.py                 # Main Flask application
├── camera.py              # Camera handling module
├── config.py              # Configuration settings
├── detector.py            # YOLO detection logic
├── logger.py              # Violation logging
├── requirements.txt       # Python dependencies
├── yolov8n.pt             # YOLOv8 model weights
├── static/                # Static files (CSS, JS)
├── templates/             # HTML templates
│   └── index.html
├── logs/                  # Log files
│   └── violations.csv
└── __pycache__/           # Python cache
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 🚀

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you have any questions or issues, please open an issue on GitHub. 🆘