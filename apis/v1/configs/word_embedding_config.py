from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv 
load_dotenv()

mxbai_embedder = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")
