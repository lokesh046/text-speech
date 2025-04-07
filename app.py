import os
import streamlit as st
from transformers import pipeline

# Streamlit app title
st.title("🧠 Building Generative AI Tool")

st.markdown("""
The pipelines are a great and easy way to use models for inference. These pipelines are objects that abstract most of the 
complex code from the library, offering a simple API dedicated to several tasks, including Named Entity Recognition, 
Masked Language Modeling, Sentiment Analysis, Feature Extraction and Question Answering.
""")

st.subheader("🔊 Converting Text to Speech")

# Text input
text = st.text_input("Enter your text here...", value="Hello! Welcome to your generative AI tool.")

# Hugging Face auth token via environment variable (safe practice)
hf_token = os.getenv(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)

if text:
    try:
        # Load text-to-speech pipeline
        pipe = pipeline("text-to-speech", model="espnet/kan-bayashi_ljspeech_vits", use_auth_token=hf_token)
        output = pipe(text)
        st.audio(output["audio"], sample_rate=output["sampling_rate"])
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

