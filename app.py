import streamlit as st
import torch
import cv2

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="YOLO Fruit & Vegetable Detector",
    layout="wide"
)

st.title("🍌🥔 YOLO Real-Time Detection")
st.write("Fruit | Vegetable")

# ==============================
# SESSION STATE
# ==============================
if "run" not in st.session_state:
    st.session_state.run = False

# ==============================
# BUTTONS
# ==============================
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Start Camera"):
        st.session_state.run = True

with col2:
    if st.button("⏹ Stop Camera"):
        st.session_state.run = False

# ==============================
# LOAD YOLOv5 MODEL
# ==============================
@st.cache_resource
def load_model():
    model = torch.hub.load(
        repo_or_dir='yolov5',
        model='custom',
        path=r'C:\Users\Luqman\Desktop\yolo_web_gui\yolov5\runs\train\exp18\weights\best.pt',
        source='local'
    )
    model.conf = 0.25
    model.iou  = 0.45
    return model

model = load_model()

# ==============================
# CLASS ID MAPPING (IMPORTANT)
# ==============================
BANANA_ID = [k for k, v in model.names.items() if v == 'banana'][0]
POTATO_ID = [k for k, v in model.names.items() if v == 'potato'][0]

# ==============================
# DISPLAY AREA
# ==============================
frame_window = st.image([])
info_box = st.empty()

# ==============================
# CAMERA LOOP
# ==============================
if st.session_state.run:
    cap = cv2.VideoCapture(1)   # tukar 0 jika webcam lain

    if not cap.isOpened():
        st.error("❌ Camera tak boleh dibuka")
    else:
        while st.session_state.run:
            ret, frame = cap.read()
            if not ret:
                st.warning("⚠️ Frame gagal dibaca")
                break

            # ==============================
            # YOLO INFERENCE
            # ==============================
            results = model(frame)
            df = results.pandas().xyxy[0]

            # ==============================
            # FILTER CONFIDENCE (CLASS-SPECIFIC)
            # ==============================
            df = df[
                ((df['name'] == 'banana') & (df['confidence'] >= 0.5)) |
                ((df['name'] == 'potato') & (df['confidence'] >= 0.35))
            ]

            # ==============================
            # COUNT OBJECT
            # ==============================
            banana = (df['name'] == 'banana').sum()
            potato = (df['name'] == 'potato').sum()

            # ==============================
            # INFO DISPLAY
            # ==============================
            if banana == 0 and potato == 0:
                info_box.error("❌ No detection")
            else:
                info_box.success(
                    f"🍌 Banana(FRUIT) : {banana}\n\n"
                    f"🥔 Potato(VEGETABLE) : {potato}"
                )

            # ==============================
            # REMOVE FALSE BANANA BOXES (RENDER FILTER)
            # ==============================
            pred = results.xyxy[0]

            pred = pred[
                ((pred[:, 5] == BANANA_ID) & (pred[:, 4] >= 0.5)) |
                ((pred[:, 5] == POTATO_ID) & (pred[:, 4] >= 0.35))
            ]

            results.xyxy[0] = pred

            # ==============================
            # RENDER RESULT
            # ==============================
            frame = results.render()[0]
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_window.image(frame)

        cap.release()
