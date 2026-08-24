from ultralytics import YOLO
import os

def run_diagnosis(image_path):
    # Path to the best version of your trained model
    model_path = r'runs\classify\runs\classify\skin_cancer_classifier5\weights\best.pt'
    
    if not os.path.exists(model_path):
        print("Error: Trained model weights not found!")
        return

    model = YOLO(model_path)

    # Run the prediction
    results = model.predict(source=image_path)

    for result in results:
        # Get the highest probability result
        probs = result.probs
        top1_idx = probs.top1
        class_name = result.names[top1_idx]
        confidence = probs.top1conf.item()
        
        print("-" * 30)
        print(f"DIAGNOSIS: {class_name}")
        print(f"CONFIDENCE: {confidence*100:.2f}%")
        print("-" * 30)
        
        # Display the result visually
        result.show()

if __name__ == '__main__':
    # Place any skin image on your desktop and put the filename here
    test_image = r'C:\Users\sanab\OneDrive\Desktop\Skin_Cancer_Project\data\val\basal cell carcinoma\ISIC_0000084.jpg' 
    if os.path.exists(test_image):
        run_diagnosis(test_image)
    else:
        print(f"Place an image at {test_image} to run a diagnosis.")