from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()
model= ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

chat_history=[
    SystemMessage('you are a helpful assistance'),
]
while True:
    user_input = input("user: ")
    chat_history.append(HumanMessage(user_input))
    if user_input=='exit':
        print(chat_history)
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.text))
    print("AI: ",result.text)