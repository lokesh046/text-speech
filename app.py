import streamlit as st
from gtts import gTTS
import os

# App Title
st.title("🗣️ Text-to-Speech Converter using gTTS")

# App Description
st.markdown("""
## 🎯 Purpose of this App
This fun and efficient Text-to-Speech (TTS) tool uses Google's `gTTS` (Google Text-to-Speech) API to convert written text into spoken words.

> 💡 *“Words mean more than what is set down on paper. It takes the human voice to infuse them with deeper meaning.” – Maya Angelou*

Just enter your text, select a **voice character**, and press play!

---
""")

# Input Section
st.header("✍️ Enter Your Text")
text = st.text_input("📌 Type something you'd like to convert into speech:", "")

# Voice Character Selection (for visual/fun purpose)
st.header("🎭 Choose a Voice Character")

character_styles = {
    "🤖 Robot Voice": "en",
    "🎩 British Gentleman": "en",
    "🎙️ Movie Narrator": "en",
    "😆 Cartoon Character": "en",
    "👩‍🏫 School Teacher": "en",
    "🧙 Wizard": "en"
}
character_choice = st.selectbox("🎧 Select a character:", list(character_styles.keys()))
selected_lang = character_styles[character_choice]

# TTS Processing
if text:
    tts = gTTS(text=text, lang=selected_lang, slow=False)
    tts.save("output.mp3")

    # Play Audio
    st.success(f"✅ Here's how your text sounds as a {character_choice}!")
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# Footer
st.mark

