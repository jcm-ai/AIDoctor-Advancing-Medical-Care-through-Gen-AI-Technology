import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from src.helper import download_hugging_face_embeddings
from src.prompt import *
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

embeddings = download_hugging_face_embeddings()

index_name = "aidoctor"

# Load Existing index and embed each chunk into the Pinecone index
docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)