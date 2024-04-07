import streamlit as st
from transformers import pipeline

st.title("Simple Text Generation")
user_input = st.text_input("Enter your text here:")

if st.button("Generate text"):
    generator = pipeline("text-generation", model="gpt2")
    text = generator(user_input, max_length=100)[0]["generated_text"]
    st.write(text)