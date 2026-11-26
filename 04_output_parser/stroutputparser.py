from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')

template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='write a 5 line summery on the following text. /n {text}',
    input_variables=['text']
)

prompt1=template1.invoke({'topic':'artifitial intelligence'})
res=model.invoke(prompt1)

prompt2=template2.invoke({'text':res.text})
res2=model.invoke(prompt2)

print(res2.text)