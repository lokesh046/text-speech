from gtts import gTTS
import streamlit as st
import os

# App Title and Description
st.title("🎙️ Text-to-Speech Generator")
st.markdown("""
Welcome to the **Text-to-Speech Generator** powered by `gTTS`.

Enter your text below, choose a voice (character), and instantly convert it to audio!
""")

# Input text
text = st.text_input("✍️ Enter your text here")

# Character Selection (Voice Style)
st.subheader("🎭 Choose a Character Voice")
character = st.selectbox("
