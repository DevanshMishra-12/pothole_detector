# pothole_detector

🕳️ Pothole Detection App
This is a simple Streamlit web app that detects potholes in images using a Roboflow YOLOv8 model.
You upload an image → the app sends it to Roboflow → receives predictions → shows the result with bounding boxes.

⭐ Features
Upload an image
Detect potholes using a trained YOLOv8 model
View the image with detection boxes
Download the output image
Works on Streamlit Cloud

📁 Project Structure
project/
│
├── pothol2.py          # Main Streamlit app
├── requirements.txt    # Dependencies
└── README.md           # Documentation

📦 Requirements
Your requirements.txt should contain:
streamlit
requests
pillow

🚀 How to Run Locally
Clone the project
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


Install dependencies
pip install -r requirements.txt
Run the app
streamlit run pothol2.py

🔑 Roboflow Setup
To make the app work:
Go to your Roboflow project
Open Deploy → Hosted API

Copy:
Your API Key
The Model ID (example: pothole-detection-yolov8/1)
Update these in your code:

API_KEY = "YOUR_API_KEY"
MODEL_ID = "pothole-detection-yolov8/1"

☁️ Deploying on Streamlit Cloud
Push your project to GitHub
Go to share.streamlit.io
Select your repo
Deploy the app
Streamlit installs packages and runs pothol2.py

🧪 How It Works (Simple)
User uploads an image
The app sends the image to Roboflow API
Roboflow returns predicted bounding boxes
The app draws the boxes using Pillow
Final image is shown and can be downloaded

🛠️ Troubleshooting
No predictions / errors?
Check your API key
Check model ID
Check if your Roboflow account has credits
