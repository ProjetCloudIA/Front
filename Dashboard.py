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
    uploaded_file = st.file_uploader('Upload a file', type=['png', 'jpg', 'jpeg'])
    if(uploaded_file):
        image = Image.open(uploaded_file)
        img_bytes = io.BytesIO()
        image.save(img_bytes, format=image.format)
        img_bytes = img_bytes.getvalue()
        try:
            response = requests.post("https://api-cloud-dfc87ab4de89.herokuapp.com/predict", files={"file": img_bytes})
            result = response.json()['prediction'][0]

            if(result=="surprise"):
                st.success('Surprise 😯')
            elif(result=="sad"):
                st.success('Sad 😭')
            elif(result=="neutral"):
                st.success('Neutral 😐')
            elif(result=="happy"):
                st.success('Happy 😊')
            elif(result=="fear"):
                st.success('Fear 😨')
            elif(result=="disgust"):
                st.success('Disgust 🤢')
            elif(result=="angry"):
                st.success('Angry 😡')
            
        except:
            st.error('Failed to create a new record')
    st.form_submit_button("Predict")


# URL du WebSocket de l'API FastAPI
WS_URL = "ws://api-cloud-g1-177dac7611b1.herokuapp.com/ws"  # Remplace par l'URL correcte

st.title("🎥 Flux Vidéo en Direct + Prédiction")

# Conteneur pour afficher l'image et la prédiction
image_placeholder = st.empty()
prediction_placeholder = st.empty()

async def stream_video():
    """Envoie les images de la webcam à l'API WebSocket et affiche la prédiction."""
    async with websockets.connect(WS_URL) as websocket:
        cap = cv2.VideoCapture(0)  # Ouvre la webcam

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Convertir l'image OpenCV en PIL
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image_pil = Image.fromarray(frame_rgb)

                # Encoder l'image en binaire
                img_bytes = io.BytesIO()
                image_pil.save(img_bytes, format="JPEG")
                img_bytes = img_bytes.getvalue()

                # Envoyer l'image à l'API WebSocket
                await websocket.send(img_bytes)

                # Réception de la prédiction
                response = await websocket.recv()
                prediction = json.loads(response).get("prediction", "Aucune prédiction")

                # Mise à jour de l'affichage Streamlit
                image_placeholder.image(image_pil, caption="Flux en direct", use_container_width=True)
                result_stream = prediction[0]
                text_to_write = ''
                if(result_stream=="surprise"):
                    text_to_write='Surprise 😯'
                elif(result_stream=="sad"):
                    text_to_write='Sad 😭'
                elif(result_stream=="neutral"):
                    text_to_write='Neutral 😐'
                elif(result_stream=="happy"):
                    text_to_write='Happy 😊'
                elif(result_stream=="fear"):
                    text_to_write='Fear 😨'
                elif(result_stream=="disgust"):
                    text_to_write='Disgust 🤢'
                elif(result_stream=="angry"):
                    text_to_write='Angry 😡'
                prediction_placeholder.write(f"**Prédiction :** {text_to_write}")

                # await asyncio.sleep(0.05)  # Pause pour éviter de surcharger l'API

        finally:
            cap.release()

# Lancer la boucle d'événements Asyncio
asyncio.run(stream_video())



