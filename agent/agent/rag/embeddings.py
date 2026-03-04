import os
from docx import Document
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

def read_docx(filepath):
    doc = Document(filepath)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def upload_documents(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]
    print(f"Found {len(files)} documents")
    vectors = []
    for filename in files:
        filepath = os.path.join(folder_path, filename)
        print(f"Processing: {filename}")
        text = read_docx(filepath)
        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            vector = embeddings.embed_query(chunk)
            doc_id = filename.encode('ascii', 'ignore').decode('ascii').replace(' ', '_').replace('—', '')
            vectors.append({
                "id": f"{doc_id}_{i}",
                "values": vector,
                "metadata": {"text": chunk, "source": filename}
            })
    index.upsert(vectors=vectors)
    print(f"✅ Uploaded {len(vectors)} chunks to Pinecone!")

upload_documents("Documents for the pinecone")