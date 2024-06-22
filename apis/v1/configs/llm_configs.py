import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

gpt_model = ChatOpenAI(api_key=os.environ.get('OPENAI_API_KEY'), temperature=0,
                       request_timeout=120, streaming=True, model="gpt-3.5-turbo-0125")
gemini_model = ChatGoogleGenerativeAI(api_key=os.environ.get(
    'GOOGLE_API_KEY'), temperature=0, model="gemini-pro", request_timeout=120)
