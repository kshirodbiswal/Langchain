from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="delhi is the capital of india"
document=["delhi is the capital of india","bbsr is the capital of odisha","paris is the capital of france"]

vector_text=embedding.embed_query(text)
vector_document=embedding.embed_documents(document)

print("text:",str(vector_text))
print("document:",str(vector_document))
