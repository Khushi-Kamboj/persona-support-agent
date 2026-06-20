from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

import os
from dotenv import load_dotenv
from google import genai

import chromadb

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chroma_client = chromadb.PersistentClient(
    path="./vector_db/chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="support_kb"
)

def load_documents(data_folder="data"):

    documents = []

    for file in Path(data_folder).glob("*"):

        if file.suffix in [".txt", ".md"]:

            with open(file, "r", encoding="utf-8") as f:

                documents.append({
                    "source": file.name,
                    "content": f.read()
                })

        elif file.suffix == ".pdf":

            reader = PdfReader(str(file))

            pdf_text = ""

            for page in reader.pages:
                pdf_text += page.extract_text() + "\n"

            documents.append({
                "source": file.name,
                "content": pdf_text
            })

    return documents


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for doc in documents:

        split_chunks = splitter.split_text(
            doc["content"]
        )

        for idx, chunk in enumerate(split_chunks):

            chunks.append({
                "id": f"{doc['source']}_{idx}",
                "source": doc["source"],
                "text": chunk
            })

    return chunks

def get_embedding(text):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values

def retrieve_context(query, top_k=3):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    contexts = []

    for i in range(
        len(results["documents"][0])
    ):

        contexts.append({
            "text":
            results["documents"][0][i],

            "source":
            results["metadatas"][0][i]["source"]
        })

    return contexts

def ingest_chunks(chunks):

    for chunk in chunks:

        embedding = get_embedding(
            chunk["text"]
        )

        collection.add(
            ids=[chunk["id"]],
            documents=[chunk["text"]],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": chunk["source"]
                }
            ]
        )

    print(
        f"Stored {len(chunks)} chunks in ChromaDB"
    )

if __name__ == "__main__":

    # 1. Load docs
    docs = load_documents()

    print(f"Loaded {len(docs)} documents")

    # 2. Create chunks
    chunks = chunk_documents(docs)

    print(f"Created {len(chunks)} chunks")

    # 3. Store in ChromaDB
    ingest_chunks(chunks)

    print("Total Records:", collection.count())

    # 4. Test query
    query = "How do I reset my password?"

    results = retrieve_context(query)

    print("\nRetrieved Chunks:\n")

    for item in results:

        print("=" * 50)

        print("Source:", item["source"])

        print(item["text"][:300])