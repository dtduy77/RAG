import dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
dotenv.load_dotenv()

chat_history = ChatMessageHistory()
gemini_model = ChatGoogleGenerativeAI(google_api_key=os.environ.get("GOOGLE_API_KEY"), model="gemini-1.5-pro-latest", temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | gemini_model

chat_history.add_user_message(
    "Translate this sentence from English to French: I love programming."
)

response = chain.invoke({"messages": chat_history.messages})
chat_history.add_ai_message(response)
chat_history.add_user_message("What did you just say?")

res = chain.invoke({"messages": chat_history.messages})

print(res.content)