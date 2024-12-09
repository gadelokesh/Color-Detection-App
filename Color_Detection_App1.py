import streamlit as st
import cv2
import numpy as np

# Set the page configuration for a beautiful header
st.set_page_config(
    page_title=" Color Detection App ",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add some custom styles for the app
st.markdown("""
    <style>
        body {
            background-color: #0A0B0D;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            border-radius: 8px;
            padding: 15px 35px;
            font-size: 20px;
            margin-top: 15px;
        }
        .stButton>button:hover {
            background-color: #005f6a;
        }
        .stRadio>label, .stSelectbox>label {
            color: white;
            font-size: 18px;
        }
        .stSlider>label {
            color: white;
            font-size: 16px;
        }
        .header-text {
            text-align: center;
            font-size: 36px;
            color: #FF6F61;
            font-weight: bold;
        }
        .highlight {
            color: #ff9800;
        }
        .image-box {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #1F1F1F;
            border-radius: 10px;
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Title and Introduction
st.markdown('<p class="header-text">✨ Color Detection App</p>', unsafe_allow_html=True)

st.write("""
    Welcome to the **Color Detection App!** 🎨
    Choose a color mode to detect (Red, Green, Blue) or create your own custom color using the sliders.
    Use the webcam to detect specific colors in real-time.
""")

# Sidebar section for color mode selection
st.sidebar.header("Select Color Detection Mode")

color_mode = st.sidebar.radio(
    "Choose a color mode to detect:",
    ("Red", "Green", "Blue", "Custom")
)

# Handle custom color detection mode
if color_mode == "Custom":
    st.sidebar.write("Adjust the sliders below to create a custom color mode.")
    low_hue = st.sidebar.slider("Low Hue", 0, 179, 0)
    high_hue = st.sidebar.slider("High Hue", 0, 179, 179)
    low_saturation = st.sidebar.slider("Low Saturation", 0, 255, 0)
    high_saturation = st.sidebar.slider("High Saturation", 0, 255, 255)
    low_value = st.sidebar.slider("Low Value", 0, 255, 0)
    high_value = st.sidebar.slider("High Value", 0, 255, 255)
else:
    # Predefined color bounds
    if color_mode == "Red":
        low_hue, high_hue, low_saturation, high_saturation, low_value, high_value = [161, 179, 155, 255, 84, 255]
    elif color_mode == "Green":
        low_hue, high_hue, low_saturation, high_saturation, low_value, high_value = [25, 102, 52, 255, 72, 255]
    elif color_mode == "Blue":
        low_hue, high_hue, low_saturation, high_saturation, low_value, high_value = [94, 126, 80, 255, 2, 255]

# Function to run the webcam and detect color
def detect_color(mode):
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Set custom or predefined color bounds
        low_bound = np.array([low_hue, low_saturation, low_value])
        high_bound = np.array([high_hue, high_saturation, high_value])

        mask = cv2.inRange(hsv_frame, low_bound, high_bound)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Show webcam feed and color detection result
        cv2.imshow(f"{mode} Color Detection", result)
        cv2.imshow("Original Webcam Feed", frame)

        # Exit the loop when ESC is pressed
        key = cv2.waitKey(1)
        if key == 27:  # ESC key to stop the webcam
            break
    cap.release()
    cv2.destroyAllWindows()

# Action buttons for user interaction
if st.button(f"Start Detection for {color_mode}"):
    st.write(f"Detecting **{color_mode}** Color...")
    detect_color(color_mode)



# Footer
st.markdown("---")
st.markdown("© 2024 Developed by **L**")