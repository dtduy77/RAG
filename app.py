# app.py
import streamlit as st
import requests

# Define the FastAPI endpoint URL
FASTAPI_URL = "http://localhost:7860/api/v1/rag/upload"

st.title("Document Summarizer")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Text input for the question
question = st.text_input("Enter your question")

# Button to submit the file and question
if st.button("Get Summary"):
    if uploaded_file and question:
        # Use a form to submit the file and question
        with st.spinner('Processing...'):
            files = {"doc": uploaded_file.getvalue()}
            response = requests.post(FASTAPI_URL, files={"doc": uploaded_file}, data={"question": question})
            
            if response.status_code == 200:
                result = response.json()
                st.success("Response received successfully!")
                st.write(result["data"])
            else:
                st.error(f"Error: {response.status_code}")
                st.write(response.json())
    else:
        st.warning("Please upload a file and enter a question.")

        