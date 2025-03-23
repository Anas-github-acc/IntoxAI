from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

def create_rag_chain(vectorstore):
    # prompt template
    prompt_template = """Use the following pieces of context to answer the queries of the user. If you don't know the answer, just say so and be genuine.

Context: {context}

Question: {question}

Answer:"""
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    # loading openai model
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Create the RAG chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        chain_type_kwargs={"prompt": PROMPT}
    )
    return chain

# Mock response function (no longer needed but kept for reference)
def mock_openai_response(query, context):
    if "mission" in query.lower():
        return "xAI's mission is to accelerate human scientific discovery."
    elif "products" in query.lower():
        return "xAI builds tools like Grok, a conversational AI."
    elif "grok" in query.lower():
        return "Grok uses advanced AI to provide helpful answers."
    else:
        return f"Based on the context:\n{context}\n\nI don't have a precise answer for '{query}'."