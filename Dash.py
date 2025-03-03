import streamlit as st
import cv2
import requests
import numpy as np
import base64
import time

st.title("🧠 Prédiction IA via API en temps réel")

# URL de l'API (exemple)
API_URL = "https://api-cloud-g1-177dac7611b1.herokuapp.com/predict"

# Ouvrir la webcam avec OpenCV
cap = cv2.VideoCapture(0)

# Vérifier si la webcam s'ouvre bien
if not cap.isOpened():
    st.error("❌ Impossible d'ouvrir la webcam. Vérifie tes permissions.")
    st.stop()

def send_frame_to_api(image):
    """Envoie une image à l'API et récupère la prédiction."""
    _, img_encoded = cv2.imencode(".jpg", image)  # Convertir en JPEG
    img_base64 = base64.b64encode(img_encoded.tobytes()).decode("utf-8")  # Encoder en Base64

    try:
        response = requests.post(API_URL, json={"image": img_base64}, timeout=5)
        if response.status_code == 200:
            return response.json()  # Retourne la réponse JSON de l'API
    except requests.exceptions.RequestException:
        return {"error": "API non disponible"}

    return {"error": "API non disponible"}

# Interface pour afficher la caméra
frame_placeholder = st.empty()

while True:
    ret, frame = cap.read()
    if not ret:
        st.error("❌ Impossible de lire la caméra.")
        break

    # Envoyer l'image à l'API et récupérer la prédiction
    api_response = send_frame_to_api(frame)

    # Vérifier la réponse et afficher le résultat
    if "prediction" in api_response:
        prediction_text = api_response["prediction"]
        cv2.putText(frame, prediction_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Convertir en RGB pour Streamlit
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Afficher l'image dans Streamlit
    frame_placeholder.image(frame, channels="RGB", use_container_width=True)

    # Petite pause pour éviter de surcharger la CPU
    time.sleep(0.05)

# Libérer la webcam
cap.release()
