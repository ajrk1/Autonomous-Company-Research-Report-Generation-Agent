import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)

def retrieve(query, top_k=5):
    try:
        vector = embeddings.embed_query(query)
        results = index.query(vector=vector, top_k=top_k, include_metadata=True)
        chunks = []
        for match in results["matches"]:
            text = match.get("metadata", {}).get("text", "")
            if text:
                chunks.append(text)
        return chunks if chunks else ["No guidance found."]
    except Exception as e:
        return ["RAG error: " + str(e)]