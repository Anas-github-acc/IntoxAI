from dotenv import load_dotenv
import os
from src.ingest import ingest_documents
from src.rag_chain import create_rag_chain

load_dotenv()

def main():
    cohere_api_key = os.getenv("COHERE_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    langsmith_api_key = os.getenv("LANGSMITH_API_KEY")

    if not cohere_api_key:
        print("Error: COHERE_API_KEY not found in .env file.")
        return
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in .env file.")
        return
    if os.getenv("LANGSMITH_TRACING") == "true" and not langsmith_api_key:
        print("Warning: LANGSMITH_TRACING is true but LANGSMITH_API_KEY is missing. Tracing disabled.")

    print("Ingesting documents...")
    vectorstore = ingest_documents("data/faq.txt")
    
    print("Setting up RAG chain...")
    rag_chain = create_rag_chain(vectorstore)

    print("Welcome to the xAI FAQ RAG System! Ask a question (or type '/quit' or '/bye' to exit):")
    while query := input("> "):
        if query.lower() == '/quit' or query.lower() == '/bye':
            break
        response = rag_chain(query)
        print(response)
    print("Goodbye!")

if __name__ == "__main__":
    main()