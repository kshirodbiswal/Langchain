from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.5,
)  # Lower values are more deterministic; higher values are more creative.
result=chatmodel.invoke("write a poem on football in hinglish")

print(result)


# | Use Case | Recommended Temperature |
# | :--- | :--- |
# | Factual answers (math, code, facts) | 0.0 - 0.3 |
# | Balanced response (general QA, explanations) | 0.3 - 0.7 |
# | Creative writing, storytelling, jokes | 0.7 - 1.2 |
# | Maximum randomness (wild ideas, brainstorming) | 1.5+ |