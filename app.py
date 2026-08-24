import os
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration matching your Architecture's Image Acquisition Module
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Path to your BEST trained model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "runs" / "classify" / "runs" / "classify" / "skin_cancer_classifier5" / "weights" / "best.pt"

model = YOLO(str(MODEL_PATH))
model = YOLO(MODEL_PATH)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/info')
def information_page():
    return render_template('info.html')

@app.route('/upload', methods=['GET', 'POST'])
def diagnostic_upload():  # Renamed to avoid Flask conflict
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # YOLOv8 Inference (Output Module) [cite: 139]
            results = model.predict(source=filepath)
            
            for result in results:
                probs = result.probs
                label = result.names[probs.top1]
                confidence = float(probs.top1conf.item())

            return render_template('result.html', 
                                   label=label, 
                                   conf_val=round(confidence * 100, 2), 
                                   img=filename)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)