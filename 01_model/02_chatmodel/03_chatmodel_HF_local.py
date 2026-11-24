from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-intermediate-step-240k-503b",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
    ),
)

model = ChatHuggingFace(llm=llm)
res = model.invoke("what is the capital of odisha?")
print(res.content)