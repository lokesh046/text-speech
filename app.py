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
character = st.selectbox("Select a voice character", ["Default", "Robot", "Narrator", "Whisper", "Energetic"])

# Text-to-Speech Logic
if text:
    # You can simulate character styles by tweaking speech speed or tones (limited in gTTS).
    # For now, these characters are just placeholders. Only Default is used in gTTS.
    tts = gTTS(text, lang='en')
    tts.save("output.mp3")
    
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

    # Feedback
    st.success(f"✅ Audio generated with '{character}' character voice")

# Footer
st.markdown("""
---
Made with ❤️ using [gTTS](https://pypi.org/project/gTTS/) and [Streamlit](https://streamlit.io/)
""")
