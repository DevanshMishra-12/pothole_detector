import streamlit as st
from inference_sdk import InferenceHTTPClient
import cv2
import numpy as np
from PIL import Image
import tempfile
import os

# ----------------------------
# 1. Streamlit App Title
# ----------------------------
st.set_page_config(page_title="Pothole Detection App", page_icon="🕳️", layout="centered")
st.title("Pothole Detection using Roboflow YOLOv8")

st.write("Upload an image to detect potholes using a pre-trained Roboflow model.")

# ----------------------------
# 2. Setup Roboflow Client
# ----------------------------
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="XSyZlOZklNYWxElOLpgK"  # Replace with your own Roboflow API key if needed
)

# ----------------------------
# 3. File Upload Section
# ----------------------------
uploaded_file = st.file_uploader("Upload an image (jpg, png, webp):", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    # ----------------------------
    # 4. Run Inference
    # ----------------------------
    with st.spinner("🔍 Running detection... Please wait..."):
        result = CLIENT.infer(
            temp_path,
            model_id="pothole-detection-yolov8/1"
        )

    st.success(" Detection complete!")

    # ----------------------------
    # 5. Draw Bounding Boxes
    # ----------------------------
    img = cv2.imread(temp_path)
    for pred in result['predictions']:
        x, y, w, h = int(pred['x']), int(pred['y']), int(pred['width']), int(pred['height'])
        conf = pred['confidence']
        cls = pred['class']

        x1, y1 = x - w // 2, y - h // 2
        x2, y2 = x + w // 2, y + h // 2

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{cls} {conf:.2f}"
        cv2.putText(img, label, (x1, max(20, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Convert BGR to RGB for Streamlit
    annotated_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ----------------------------
    # 6. Display Results
    # ----------------------------
    st.image(annotated_img, caption="Detected Potholes", use_container_width=True)

    # Option to download
    result_path = "result_with_boxes.jpg"
    cv2.imwrite(result_path, img)

    with open(result_path, "rb") as file:
        st.download_button(
            label="📥 Download Result Image",
            data=file,
            file_name="result_with_boxes.jpg",
            mime="image/jpeg"
        )

    # Clean temporary files
    os.remove(temp_path)

