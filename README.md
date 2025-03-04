# 🎭 Emotion Detection avec Streamlit

Ce projet est une application web interactive permettant de capturer une image via la caméra et d'analyser l'émotion du visage détecté grâce à une API d'intelligence artificielle.

## 🚀 Fonctionnalités
- 📸 Capture d'image en direct via la caméra
- 📡 Envoi de l'image à une API pour l'analyse d'émotion
- 📊 Affichage de l'émotion détectée avec des emojis
- 🖼️ Visualisation de l'image capturée

## 🛠️ Installation
### 1️⃣ Cloner le projet
```bash
git clone https://github.com/votre-repo/emotion-detection.git
cd emotion-detection
```

### 2️⃣ Installer les dépendances
Assurez-vous d'avoir Python installé, puis exécutez :
```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application
```bash
streamlit run app.py
```

## 🏗️ Structure du projet
```
📂 emotion-detection
│── 📄 app.py          # Code principal Streamlit
│── 📄 requirements.txt # Liste des dépendances
│── 📄 README.md       # Documentation
```

## Liens du projet
- **FRONT** : `https://front-cloud-g1-c1cec2c6a66e.herokuapp.com/`
- **API** : `https://api-cloud-g1-177dac7611b1.herokuapp.com/`
- **MLFLOW** :: `https://mlflow-cloud-g1-1d0d7b4ea267.herokuapp.com/`

## 📡 API utilisée
L'application envoie les images capturées à une API d'analyse des émotions :
- **URL** : `https://api-cloud-dfc87ab4de89.herokuapp.com/predict`
- **Méthode** : POST
- **Paramètre** : `file` (image en format binaire)
- **Réponse** : JSON contenant l'émotion prédite

## 🎨 Résultats possibles
| Émotion  | Emoji |
|----------|-------|
| Surprise | 😯 |
| Tristesse | 😭 |
| Neutre | 😐 |
| Joie | 😊 |
| Peur | 😨 |
| Dégoût | 🤢 |
| Colère | 😡 |

## 📜 Licence
Ce projet est sous licence **MIT**.

---
✨ Créé avec ❤️ et Streamlit ✨
