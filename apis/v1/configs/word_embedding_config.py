from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv 
load_dotenv()

mxbai_embedder = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")

google_embedder = GoogleGenerativeAIEmbeddings(google_api_key=os.environ.get("GOOGLE_API_KEY"), model="models/embedding-001")