import streamlit as st
from groq import Groq

# Set page config
st.set_page_config(page_title="Llama 3.3")

# Load the api key
api_key = st.secrets["API_KEY"]

# Create an instance of groq client
client = Groq(api_key = api_key)

# Write a function to get response from the Groq client
def model_response(text: str):
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assitant"
            },
            {
                "role": "user",
                "content": text
            }
        ],
        model = "llama-3.3-70b-versatile",
        stream= True
    )

    for chunk in stream:
        reponse = chunk.choices[0].delta.content
        if reponse is not None:
            yield reponse

# Start building streamlit app
st.title("Llama 3.3 Model")
st.subheader("by Utkarsh Gaikwad")

text = st.text_area("Please ask any question : ")

if text:
    st.subheader("Model Response : ")
    st.write_stream(model_response(text))
