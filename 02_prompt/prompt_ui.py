from pathlib import Path
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model=GoogleGenerativeAI(model="gemini-3.5-flash-lite")
st.header("research tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Select...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template_path = Path(__file__).parent / "template.json"
template = load_prompt(template_path)


if st.button('summerize'):
     chain=template | model  #combinging multiple steps using chains
     result=chain.invoke({
           'paper_input':paper_input,
           'style_input':style_input,
           'length_input':length_input,
     })
     st.write(result)