# 🍌🥔 Banana & Potato Object Detection using YOLO

## 📌 Project Overview

This project presents a YOLO-based object detection system developed as a case study to detect two object classes: **Banana** and **Potato**.

The system uses a custom annotated dataset and includes a Streamlit-based web GUI that allows users to upload images and perform object detection interactively.

---

## 🛠️ Technologies Used

- Python
- Ultralytics YOLOv8
- Streamlit (Web GUI)
- OpenCV
- Custom YOLO Dataset

---

## 📁 Dataset

Due to GitHub file size limitations, the dataset is hosted externally.

🔗 Download Dataset:
https://drive.google.com/drive/folders/17Ne3hZQsqt0QWw167yG6L1J6rZtcsR6n?usp=sharing

Classes:
- 0: Banana
- 1: Potato

---

## 🚀 How to Run the Application (Streamlit GUI)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

---

### 2️⃣ Install Dependencies

```bash
pip install ultralytics streamlit opencv-python pillow
```

---

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

After running the command, the browser will automatically open at:

```
http://localhost:8501
```

You can now upload an image and perform Banana & Potato detection.

---

## 🖥️ GUI Features

- Upload image via web interface
- Perform YOLO object detection
- Display bounding boxes
- Show confidence scores
- Real-time result visualization

---

## 📂 Important Files

- `app.py` → Streamlit web interface
- `best.pt` → Trained YOLO model weights
- `data.yaml` → Dataset configuration file

---

## 🔍 How It Works

1. User uploads an image.
2. The trained YOLO model processes the image.
3. The system detects Banana or Potato.
4. Bounding boxes and confidence scores are displayed.
5. The result is shown directly in the web interface.

---

## 🚀 Future Improvements

- Add multi-class fruit detection
- Enable webcam live detection
- Deploy the application online (Streamlit Cloud)
- Optimize model performance

---

## 📌 Conclusion

This project demonstrates the implementation of a YOLO-based object detection system integrated with a Streamlit web interface. It highlights practical Deep Learning workflow including dataset preparation, model training, evaluation, and deployment through a user-friendly interface.
