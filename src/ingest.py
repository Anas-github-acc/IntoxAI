from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import CohereEmbeddings
from langchain import tiktoken

def ingest_documents(file_path):
    # Load the FAQ text file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=tiktoken.get_encoding("cl100k_base").encode
    )
    split_docs = text_splitter.split_documents(documents)

    # Embed and store in Chroma
    embeddings = CohereEmbeddings(model="embed-english-light-v3.0")
    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        collection_name="xai_faq"
    )
    return vectorstore