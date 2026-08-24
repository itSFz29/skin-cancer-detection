from ultralytics import YOLO
import torch
import os

def train_classifier():
    # Optional safety check
    assert torch.cuda.is_available(), "CUDA not available. Install CUDA-enabled PyTorch."

    print("Using GPU:", torch.cuda.get_device_name(0))

    # Load YOLOv8 Nano classification model
    model = YOLO("yolov8n-cls.pt")

    # Train on GPU
    model.train(
        data="C:/Users/sanab/OneDrive/Desktop/Skin_Cancer_Project/data",
        epochs=30,
        imgsz=224,          # classification standard
        batch=4,            # reduce if VRAM is low
        workers=0,          # Windows stability
        device=0,           # GPU (CUDA:0)
        project="runs/classify",
        name="skin_cancer_classifier",
        patience=5,         # early stopping
        pretrained=True,
        verbose=True
    )

if __name__ == "__main__":
    train_classifier()
