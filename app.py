import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from src.helper import download_hugging_face_embeddings
from src.prompt import *
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# defining the Flask application instance to create the API endpoint for the chatbot
app = Flask(__name__)

# loading the environment variables from the .env file
load_dotenv()

# loading the Pinecone API key from the environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# downloading the embeddings from the Hugging Face model
embeddings = download_hugging_face_embeddings()

# creating a Pinecone instance to connect to the Pinecone API
index_name = "aidoctor"

# Load Existing index and embed each chunk into the Pinecone index
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)

# creating a retriever to retrieve similar documents based on the embeddings
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

# loading the Llama model for generating the answers to the questions based on the retrieved documents
llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.5})

# defining the system prompt for the chatbot to provide the context to the user
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# creating a chain to retrieve similar documents or answers based on the embeddings
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# defining the route for the chatbot API endpoint
@app.route("/")
def index():
    return render_template("chat.html")

# defining the route for the chatbot API endpoint
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])

# defining the main function to run the Flask application on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080 , debug=True)