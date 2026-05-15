from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO
import cv2
import numpy as np
import os
import base64

app = FastAPI()

import glob

def find_latest_best_pt():
    # Search for all best.pt files in the runs directory
    weights = glob.glob("runs/detect/*/weights/best.pt")
    if not weights:
        return None
    # Sort by modification time to get the most recent one
    latest_weight = max(weights, key=os.path.getmtime)
    return latest_weight

def get_model():
    latest_trained = find_latest_best_pt()
    if latest_trained:
        print(f"Loading custom model from: {latest_trained}")
        return YOLO(latest_trained)
    
    print("Falling back to base YOLOv8n model.")
    return YOLO("yolov8n.pt")

import time

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    start_time = time.time()
    
    # Read the image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Run inference
    model = get_model()
    results = model(img)

    detections = []
    for r in results:
        boxes = r.boxes.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            name = model.names[cls_id]
            
            detections.append({
                "bbox": [float(x1), float(y1), float(x2), float(y2)],
                "confidence": conf,
                "class": name
            })

    latency_ms = int((time.time() - start_time) * 1000)
    return JSONResponse(content={"detections": detections, "latency_ms": latency_ms})

@app.get("/status")
async def status():
    latest_trained = find_latest_best_pt()
    return {
        "status": "ready",
        "model_path": latest_trained if latest_trained else "base_nano",
        "checkpoint_exists": latest_trained is not None
    }

# Serve static files (frontend)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
