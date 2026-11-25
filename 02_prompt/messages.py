from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model= ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

messages=[
    SystemMessage("you are a helpful assistance"),
    HumanMessage("tell me about langchain"),
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.text))

print(messages)