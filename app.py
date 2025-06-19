import streamlit as st
import os
from moviepy.editor import *

st.set_page_config(page_title="Vidéo Histoire", layout="wide")
st.title("🎬 Générateur de Vidéos Historiques")

st.markdown("Bienvenue ! Cette application vous permet de générer automatiquement une vidéo TikTok à partir d'un personnage ou thème historique.")

texte = st.text_area("📝 Entrez votre texte ou script historique")
image = st.file_uploader("🖼️ Importez une image ou illustration (optionnel)", type=["jpg", "png"])
generate = st.button("🎥 Générer la Vidéo")

if generate and texte:
    st.info("Génération en cours... (démo statique pour l'instant)")
    st.success("Vidéo générée avec succès (démo).")
