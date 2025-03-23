from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def ingest_documents(file_path):
    # Load the FAQ text file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len  # Changed from tiktoken to simpler len function
    )
    split_docs = text_splitter.split_documents(documents)

    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
  
    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embedding_function,
        collection_name="xai_faq"
    )
    
    return vectorstore