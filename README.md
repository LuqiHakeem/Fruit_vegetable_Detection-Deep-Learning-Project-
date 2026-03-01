# Fruit_vegetable_Detection-Deep-Learning-Project-
A Deep Learning-based object detection case study using YOLO to detect Banana and Potato. The model was trained on a custom annotated dataset and evaluated using standard detection metrics.

# 🍌🥔 Banana & Potato Object Detection using YOLO

## 📌 Project Overview

This project presents a Deep Learning-based object detection system developed as a case study to detect two object classes: **Banana** and **Potato** using the YOLO (You Only Look Once) architecture.

The objective of this project is to demonstrate the implementation of real-time object detection using a custom annotated dataset. Unlike traditional image classification, this system detects and localizes objects by generating bounding boxes around detected fruits.

This project serves as a foundational study for understanding modern computer vision techniques and their practical applications.

---

## 🧠 Project Objectives

- To understand the fundamentals of YOLO object detection
- To prepare and annotate a custom dataset in YOLO format
- To train a YOLO model for binary object detection
- To evaluate model performance using standard detection metrics
- To test the trained model on unseen images

---

## 🛠️ Technologies Used

- Python
- Ultralytics YOLOv8
- OpenCV
- Google Colab / Local Training Environment
- Custom annotated dataset (YOLO format)

---

## 📁 Dataset

Due to GitHub file size limitations, the full dataset is hosted externally.

This dataset was prepared specifically for a YOLO-based object detection case study to detect two object classes:

- Banana
- Potato

### 📂 Dataset Structure

```
dataset/
├── images/
│   ├── train/
│   ├── valid/
│   └── test/
├── labels/
│   ├── train/
│   ├── valid/
│   └── test/
└── data.yaml
```

Each image contains bounding box annotations stored in `.txt` files following the YOLO annotation format.

### 📥 Download Dataset

Download the complete dataset from Google Drive:

🔗 https://drive.google.com/drive/folders/17Ne3hZQsqt0QWw167yG6L1J6rZtcsR6n?usp=sharing

---

## ⚙️ Implementation Workflow

### 1️⃣ Dataset Preparation
- Images of Banana and Potato were collected.
- Bounding boxes were annotated in YOLO format.
- Dataset was split into training, validation, and testing sets.

### 2️⃣ Model Configuration
- Created `data.yaml` configuration file.
- Defined class labels:
  - 0: Banana
  - 1: Potato

### 3️⃣ Model Training
- Used pre-trained YOLOv8 nano model (`yolov8n.pt`).
- Fine-tuned using custom dataset.
- Monitored training loss and evaluation metrics.

### 4️⃣ Model Evaluation
Model performance evaluated using:
- mAP (mean Average Precision)
- Precision
- Recall

### 5️⃣ Inference / Prediction
- Tested trained model on unseen images.
- Generated bounding boxes with confidence scores.

---

## ▶️ How to Train the Model

### 1️⃣ Install Dependencies

```bash
pip install ultralytics opencv-python
```

---

### 2️⃣ Train the YOLO Model

Ensure dataset and `data.yaml` are correctly configured.

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

Explanation:
- `data.yaml` → Dataset configuration file
- `yolov8n.pt` → Pre-trained YOLOv8 nano model
- `epochs=50` → Number of training iterations
- `imgsz=640` → Image size for training

Trained weights will be saved in:

```
runs/detect/train/
```

---

## 🔍 How to Run Inference

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=sample_images/
```

Output results will be saved in:

```
runs/detect/predict/
```
---

---

## 🖥️ Graphical User Interface (GUI)

This project includes a Graphical User Interface (GUI) implemented in `app.py` that allows users to interact with the trained YOLO object detection model.

The GUI provides a simple and user-friendly interface to test the Banana and Potato detection system without using command-line commands.

---

## 🚀 How to Run the GUI

### 1️⃣ Install Dependencies

Make sure Python is installed, then install required libraries:

```bash
pip install ultralytics opencv-python pillow
```

---

### 2️⃣ Run the Application

Navigate to the project directory and run:

```bash
python app.py
```

The GUI window will open.

---

## 🔍 GUI Features

- Upload image using file selection dialog
- Run YOLO detection automatically
- Display detected Banana and Potato objects
- Show bounding boxes with confidence scores
- Display processed output image in the interface

---

## ⚙️ How It Works

1. User clicks "Upload Image"
2. The selected image is passed to the trained YOLO model (`best.pt`)
3. The model performs object detection
4. Detected objects are displayed with bounding boxes
5. Output image is shown in the GUI window

---

## 📂 Important Files

- `app.py` → Main GUI application
- `best.pt` → Trained YOLO model weights
- `data.yaml` → Dataset configuration file

---

This GUI implementation transforms the trained YOLO model into a practical object detection application.
## 📊 Model Output

The trained model will:
- Detect Banana and Potato
- Generate bounding boxes
- Display confidence scores for each detected object

---

## 🚀 Future Improvements

- Expand to multi-class fruit detection
- Implement real-time webcam detection
- Deploy model on edge devices (e.g., Raspberry Pi)
- Improve accuracy using larger dataset

---

## 📌 Conclusion

This project demonstrates the practical implementation of YOLO-based object detection using a custom dataset. It highlights key stages in Deep Learning development including dataset preparation, model training, evaluation, and inference.

The project serves as a foundational case study for real-time computer vision applications.
