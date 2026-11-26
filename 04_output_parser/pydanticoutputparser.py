from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')

class person(BaseModel):
    name: str=Field(description='name of the person')
    age:int = Field(gt=18,description="age of the person")
    city:str = Field(description='city where the person lives')

parser=PydanticOutputParser(pydantic_object=person)

template=PromptTemplate(
    template="generate the name,age,city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions}
)

chain=template|model|parser
res=chain.invoke({'place':"british"})

print(res)