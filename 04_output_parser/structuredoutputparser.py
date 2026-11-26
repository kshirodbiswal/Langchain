from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')

schema=[
    ResponseSchema(name='fact-1',description='fact 1 about the topic'),
    ResponseSchema(name='fact-2',description='fact 2 about the topic'),
    ResponseSchema(name='fact-3',description='fact 3 about the topic')
    ]

parser=StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template='give 3 facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt=template.invoke()
chain=template|model|parser
res=chain.invoke({'topic':"AI"})

print(res)