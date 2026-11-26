from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser= StrOutputParser()

chain=template1 | model | parser | template2 |model |parser

res=chain.invoke({'topic':"artifitial intelligence"})
print(res)