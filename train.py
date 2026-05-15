from ultralytics import YOLO
import os

def train_model():
    # Initialize a YOLOv8s (Small) model - significantly more accurate than Nano
    # while still being practical for local training.
    model = YOLO('yolov8s.pt') 

    # Path to the dataset configuration
    data_path = os.path.join(os.getcwd(), 'data.yaml')

    print(f"Initializing High-Precision Training session...")

    # Start training with increased depth
    # epochs=50 for a solid production-ready model
    # patience=10 to stop if no improvement
    # imgsz=640 (standard)
    results = model.train(
        data=data_path,
        epochs=50,
        patience=10,
        imgsz=640,
        device='mps' if os.uname().machine == 'arm64' else 'cpu',
        project='runs/detect',
        name='high_precision_windmill',
        exist_ok=True,
        # Augmentations for real-world robustness
        mixup=0.1,  # Blend images
        mosaic=1.0, # Mosaic augmentation
        perspective=0.0001
    )

    print("Training complete. Weights saved to runs/detect/train_windmill/weights/best.pt")

if __name__ == "__main__":
    train_model()
