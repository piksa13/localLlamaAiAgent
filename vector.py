from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


df = pd.read_csv('realistic_restaurant_reviews.csv')  
embeddings = OllamaEmbeddings(model='mxbai-embed-large')

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
# Initialize Chroma vector store
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory=db_location,
    collection_name="restaurant_reviews"
)

if add_documents:
    vector_store.add_documents(documents= documents, ids=ids)
        
retriver = vector_store.as_retriever(
    search_kwargs={"k": 3}
    )