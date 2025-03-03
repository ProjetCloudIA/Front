import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import requests
import numpy as np
import base64

st.title("🎥 Prédiction IA via API en temps réel")

API_URL = "https://api-cloud-g1-177dac7611b1.herokuapp.com/predict"  # Mets ton URL API ici

def send_frame_to_api(image):
    """Envoie une image à l'API et récupère la prédiction."""
    _, img_encoded = cv2.imencode(".jpg", image)
    img_base64 = base64.b64encode(img_encoded.tobytes()).decode("utf-8")

    response = requests.post(API_URL, json={"image": img_base64})
    return response.json() if response.status_code == 200 else {"error": "API non disponible"}

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # Envoyer l'image à l'API et récupérer la prédiction
    api_response = send_frame_to_api(img)
    
    # Ajouter le texte de prédiction sur l'image
    if "prediction" in api_response:
        prediction_text = api_response["prediction"]
        cv2.putText(img, prediction_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

# Lancer WebRTC pour capturer la webcam du navigateur
webrtc_streamer(
    key="video-feed",
    video_frame_callback=video_frame_callback,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun1.l.google.com:19302"]},  
            {"urls": ["stun:stun2.l.google.com:19302"]},
            {"urls": ["stun:stun3.l.google.com:19302"]},
            {"urls": ["stun:stun4.l.google.com:19302"]},
            {"urls": ["stun:global.stun.twilio.com:3478"]}
        ]
    }
)
