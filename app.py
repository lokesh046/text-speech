from gtts import gTTS
import streamlit as st
import os

text = st.text_input("Enter text")

if text:
    tts = gTTS(text)
    tts.save("output.mp3")
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

