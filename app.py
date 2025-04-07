import streamlit as st
from gtts import gTTS
import os

# App Title
st.title("🗣️ Text-to-Speech Converter using gTTS")

# App Description
st.markdown("""
## 🎯 Purpose of this App
This simple and efficient Text-to-Speech (TTS) tool uses Google's `gTTS` (Google Text-to-Speech) API to convert written text into spoken words.

> 💡 *“Speech is power: speech is to persuade, to convert, to compel.” – Ralph Waldo Emerson*

Just enter your text in the box below, choose a language, and click play to hear it spoken out loud!

---
""")

# Input Section
st.header("✍️ Enter Your Text Below")
text = st.text_input("📌 Type something you'd like to convert into speech:", "")

# Language Selection
st.header("🗣️ Change Voice Language")
language_options = {
    "English (US)": "en",
    "English (UK)": "en-uk",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-cn",
    "Russian": "ru"
}
language_choice = st.selectbox("🌐 Choose a language/accent:", list(language_options.keys()))
language_code = language_options[language_choice]

# TTS Processing
if text:
    tts = gTTS(text=text, lang=language_code, slow=False)
    tts.save("output.mp3")

    # Play Audio
    st.success("✅ Conversion Successful! Click play to hear the audio.")
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# Footer
st.markdown("""
---
Made with ❤️ using [gTTS](https://pypi.org/project/gTTS/) and [Streamlit](https://streamlit.io/)
""")

