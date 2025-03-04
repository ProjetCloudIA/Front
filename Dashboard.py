import streamlit as st
import pandas as pd
import requests
from PIL import Image
import io
import cv2
import numpy as np
import time
import streamlit as st
import asyncio
import websockets
import base64
import json

st.title('Emotion Detection')

with st.form(key="my_form"):
    uploaded_file = st.file_uploader('Télécharger un fichier', type=['png', 'jpg', 'jpeg'])
    if(uploaded_file):
        image = Image.open(uploaded_file)
        st.image(image, caption="Image capturée", use_container_width=True)
        img_bytes = io.BytesIO()
        image.save(img_bytes, format=image.format)
        img_bytes = img_bytes.getvalue()
        try:
            response = requests.post("https://api-cloud-g1-177dac7611b1.herokuapp.com/predict", files={"file": img_bytes})
            result = response.json()['prediction'][0]

            emotions = {
                "surprise": "Surprise 😯",
                "sad": "Sad 😭",
                "neutral": "Neutral 😐",
                "happy": "Happy 😊",
                "fear": "Fear 😨",
                "disgust": "Disgust 🤢",
                "angry": "Angry 😡"
            }
            
            st.success(emotions.get(result, "Émotion inconnue"))
            
            
        except:
            st.error('Erreur pendant la prédiction')
    st.form_submit_button("Prédire")

st.title('Détecteur d\'émotions')

# Capture d'image avec la caméra intégrée de Streamlit
captured_image = st.camera_input("Prenez une photo")

if captured_image:
    image = Image.open(captured_image)
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()
    
    try:
        # Envoi de l'image à l'API
        response = requests.post("https://api-cloud-g1-177dac7611b1.herokuapp.com/predict", files={"file": img_bytes})
        result = response.json()['prediction'][0]
        emotions = {
            "surprise": "Surprise 😯",
            "sad": "Sad 😭",
            "neutral": "Neutral 😐",
            "happy": "Happy 😊",
            "fear": "Fear 😨",
            "disgust": "Disgust 🤢",
            "angry": "Angry 😡"
        }
        
        st.success(emotions.get(result, "Émotion inconnue"))
        
    except():
        st.error("Erreur lors de la prédiction de l'émotion.")


