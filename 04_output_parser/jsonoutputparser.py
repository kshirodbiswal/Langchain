from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')
parser=JsonOutputParser()
template=PromptTemplate(
    template='give me the name ,age,city of  a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


# prompt=template.format()
# res=model.invoke(prompt)
# res=parser.parse(res.text)

# using chains
chain=template |model|parser
res=chain.invoke({})
print(res)


