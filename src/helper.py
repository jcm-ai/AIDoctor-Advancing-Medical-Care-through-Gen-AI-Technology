from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


def load_pdf_file(directory_path):
    """
    Loads all PDF files from the specified directory.

    Parameters:
    directory_path (str): The path to the directory containing the PDF files.

    Returns:
    list: A list of documents loaded from the PDF files.
    """
    try:
        loader = DirectoryLoader(directory_path, 
                                 glob="*.pdf", 
                                 loader_cls=PyPDFLoader)
        documents = loader.load()
        return documents
    # handling exceptions if any error occurs during the process of loading the PDF files
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def text_split(extracted_text):
    """
    Splits the extracted text into chunks of 500 characters with an overlap of 20 characters.

    Args:
        extracted_text (str): The text to be split into chunks.

    Returns:
        list: A list of text chunks.
    """
    # Initialize the text splitter with specified chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    
    # Split the extracted text into chunks
    text_chunks = text_splitter.split_documents(extracted_text)

    return text_chunks



# defining a function to download embeddings from the Hugging Face model 'sentence-transformers/all-MiniLM-L6-v2'
def download_hugging_face_embeddings():
    """
    Downloads embeddings from the Hugging Face model 'sentence-transformers/all-MiniLM-L6-v2'.

    Returns:
    HuggingFaceEmbeddings: The embeddings from the specified Hugging Face model.
    """
    try:
        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        return embeddings
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
