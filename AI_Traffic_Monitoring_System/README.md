# AI Traffic Monitoring System
# 🚦 AI Traffic Monitoring & Vehicle Counting System

An AI-powered real-time traffic monitoring system built using Python, OpenCV, and YOLOv8.

This project detects and counts vehicles from live webcam or video input, captures evidence images, and logs detection timestamps. Designed for computer vision learning, smart city concepts, and engineering projects.

---

## 🎯 Features

- Real-time vehicle detection
- Detects: car, bus, truck, motorcycle
- Live vehicle count display
- Automatic image capture
- Detection timestamp logging
- Works with webcam or video file
- Lightweight YOLOv8 nano model
- Fully offline after first model download

---

## 🧠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- Pre-trained COCO dataset model

---

## 📂 Project Structure

AI_Traffic_Monitoring_System/
│
├── main.py
├── detector.py
├── config.py
├── requirements.txt
├── logs/
├── captures/
└── README.md

---

## ⚙️ Installation

1. Install Python 3.10 or later.
2. Clone the repository:

   git clone <your-repository-link>

3. Navigate to the project directory:

   cd AI_Traffic_Monitoring_System

4. Install dependencies:

   pip install -r requirements.txt

5. Run the system:

   python main.py

Note: The YOLOv8 model will automatically download during the first execution.

---

## 🖥 System Requirements

Minimum:
- Windows 11
- 8GB RAM
- Webcam or video input

Recommended:
- NVIDIA GPU for faster inference

---

## 📊 How It Works

1. Video stream is captured from webcam or file.
2. YOLOv8 detects vehicles in each frame.
3. When a vehicle is detected:
   - Bounding box is drawn
   - Vehicle count increases
   - Image is saved in /captures
   - Event is logged in /logs

---

## ⚠️ Limitations

Current version uses frame-based counting.
If the same vehicle remains in the frame, it may increase count multiple times.

Future improvements can include:
- Line-crossing vehicle counting
- Object tracking (DeepSORT)
- Traffic density analytics (vehicles/minute)
- CSV data export
- Web-based dashboard
- Heatmap visualization

---

## 🔒 Ethical & Legal Notice

This project is intended for educational and authorized research use only.
Ensure compliance with local privacy and surveillance regulations before deployment.

---

## 📈 Future Roadmap

- Advanced tracking-based counting
- Traffic congestion analysis
- Smart city dashboard integration
- Edge deployment on Raspberry Pi
- Cloud-based analytics integration

---

## 👨‍💻 Author

Developed as a computer vision and AI learning project.

Real-time vehicle detection and counting system using YOLOv8 and OpenCV.

## Features
- Detects cars, buses, trucks, motorcycles
- Real-time vehicle counting
- Saves captured images
- Logs detection timestamps
- Works with webcam or video file

## Setup

1. Install Python 3.10+
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python main.py

YOLO model will auto-download on first run.
