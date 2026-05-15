# 🔭 SkyScan AI | Industrial Infrastructure Analytics

[![AI Model](https://img.shields.io/badge/AI-YOLOv8s-00f2fe)](https://github.com/ultralytics/ultralytics)
[![UI](https://img.shields.io/badge/UI-Glassmorphism_v2.0-blueviolet)](#)
[![Status](https://img.shields.io/badge/Status-Industrial_Ready-success)](#)

SkyScan AI is a high-precision object detection platform designed to monitor and analyze industrial infrastructure. Built with **YOLOv8s** and deployed via a modern **FastAPI** backend, SkyScan identifies wind turbines, antennas, power lines, and chimneys with millisecond latency.

![SkyScan Dashboard Preview](https://github.com/radhika-verma06/SkyScan/raw/main/runs/detect/high_precision_windmill-4/results.png) *(Note: Add your own result image path here!)*

---

## ⚡ Core Features
- **Neural Infrastructure Scan**: Trained on 1,000+ specialized industrial images.
- **Micro-Latency Inference**: Real-time performance metrics (ms) built into the UI.
- **Glassmorphism V2.0 Dashboard**: A premium, futuristic interface with neon detection highlighting.
- **Cloud-Ready Training**: Includes an automated Colab pipeline for high-precision model scaling.

## 🛠️ Tech Stack
- **AI Core**: YOLOv8s (Ultralytics)
- **Backend**: FastAPI / Uvicorn / OpenCV
- **Frontend**: Vanilla JS / Glassmorphism CSS / HTML5
- **Training**: Google Colab T4 GPU

---

## 🚀 Quick Start (Local)

### 1. Clone the Repository
```bash
git clone https://github.com/radhika-verma06/SkyScan.git
cd SkyScan
```

### 2. Install Dependencies
```bash
pip install ultralytics fastapi uvicorn opencv-python-headless python-multipart
```

### 3. Launch the Engine
```bash
python3 app.py
```
Visit **`http://localhost:8000`** to start scanning.

---

## 🧠 Model Training
The project includes `windmill_training_v2.ipynb` which is optimized for Google Colab. 
- **Dataset**: 1,190 images (4 classes: `antenna`, `chimney`, `power-lines`, `wind-turbine`).
- **Precision**: 50 Epochs with advanced augmentations (Mixup/Mosaic).

## 📄 License
MIT License - Developed by Radhika Verma (3rd Year AI Student)
