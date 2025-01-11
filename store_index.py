import os
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from dotenv import load_dotenv
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

extracted_text = load_pdf_file(directory_path="data/")
text_chunks = text_split(extracted_text)
embeddings = download_hugging_face_embeddings()

# Creating Pinecone Vector Database
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "aidoctor"

pc.create_index(
    name=index_name,
    dimension=384, 
    metric="cosine", 
    spec=ServerlessSpec(
        cloud="aws", 
        region="us-east-1"
    )
)

# Embedding each chunk and upsert the embeddings into our Pinecone index.
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)

# Load Existing index and embed each chunk into the Pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,  # Name of the Pinecone index to load
    embedding=embeddings    # Embeddings to upsert into the Pinecone index
)