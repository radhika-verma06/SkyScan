# 🔭 SkyScan AI  
### Industrial Infrastructure Object Detection Platform

SkyScan AI is a computer vision platform designed to detect and analyse industrial infrastructure from images. It uses a custom-trained **YOLOv8s** object detection model to identify infrastructure classes such as wind turbines, antennas, power lines, and chimneys.

The project demonstrates applied object detection, model training, FastAPI deployment, and a modern browser-based interface for AI-powered infrastructure analysis.

---

## 🚀 Live Demo

**Live App:** https://skyscan-ods6.onrender.com

---

## ✨ Core Features

- Object detection using YOLOv8s
- Detection of industrial infrastructure classes:
  - wind turbines
  - antennas
  - power lines
  - chimneys
- FastAPI backend for image inference
- Browser-based upload and detection interface
- Real-time confidence scores and bounding boxes
- Training notebook included for model experimentation
- Designed for infrastructure monitoring and visual inspection use cases

---

## 🧠 Model Overview

SkyScan uses **YOLOv8s** from Ultralytics for object detection.

The model was trained on a specialised infrastructure image dataset containing approximately **1,190 images** across four object classes:

| Class | Description |
|---|---|
| wind-turbine | Wind turbine detection |
| antenna | Antenna and tower-like structure detection |
| power-lines | Power line detection |
| chimney | Chimney or industrial stack detection |

The training workflow was developed using Google Colab with GPU acceleration.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Model | YOLOv8s |
| Computer Vision | OpenCV |
| Backend | FastAPI, Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Training | Google Colab |
| Language | Python |
| Deployment | Render |

---

## 📦 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/radhika-verma06/SkyScan.git
cd SkyScan
```

### 2. Install dependencies

```bash
pip install ultralytics fastapi uvicorn opencv-python-headless python-multipart
```

### 3. Run the application

```bash
python3 app.py
```

The app will run locally at:

```text
http://localhost:8000
```

---

## 📁 Project Structure

```text
SkyScan/
├── app.py
├── static/
├── templates/
├── runs/
├── windmill_training_v2.ipynb
├── requirements.txt
└── README.md
```

---

## 📊 Training Workflow

The included training notebook, `windmill_training_v2.ipynb`, documents the model development process.

The training process includes:

- dataset preparation
- class labelling
- YOLOv8s model configuration
- model training
- validation
- inference testing
- result visualisation

---

## 💡 Use Cases

SkyScan can be used as a prototype for:

- infrastructure inspection
- renewable energy asset monitoring
- aerial image analysis
- industrial site review
- computer vision portfolio demonstration

---

## ⚠️ Limitations

This project is a prototype and should not be treated as a production-grade inspection system without further validation.

Current limitations include:

- limited dataset size
- performance depends on image quality and angle
- model may struggle with occluded or distant objects
- requires further testing on real-world industrial inspection data

---

## 🔮 Future Improvements

- Train on a larger and more diverse dataset
- Add precision, recall, and mAP evaluation results to the README
- Add batch image upload
- Add video inference support
- Add object count summaries
- Improve deployment reliability
- Add Docker support
- Add model version tracking

---

## 📄 License

MIT License

---

### Developed by Radhika Verma  
AI Student | Computer Vision | Applied AI Systems
