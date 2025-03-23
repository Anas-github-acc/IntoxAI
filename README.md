# IntoxAI - xAI RAG FAQ System using LangChain

A Retrieval-Augmented Generation (RAG) system for answering questions about xAI based on a pre-loaded FAQ document. This project uses LangChain for the RAG pipeline, Cohere for embeddings, Chroma as the vector store, and OpenAI for generation, with optional LangSmith tracing for monitoring.

## Project Structure

```bash
xai-rag-faq-langchain/
├── .gitignore           # Git ignore file
├── .env.template        # Template for environment variables (rename to .env)
├── data/
│   └── faq.txt          # Sample FAQ text file
├── src/
│   ├── __init__.py      # Empty file to make src a module
│   ├── ingest.py        # Loads, splits, and embeds documents into Chroma
│   └── rag_chain.py     # Sets up the RAG chain with LangChain
├── pyproject.toml       # Project configuration and dependencies
├── main.py              # Main script to run the interactive system
└── README.md            # This documentation
```

## Prerequisites

- **Python**: Version 3.9 or higher.
- **Poetry**: Dependency management tool (install instructions below).
- **API Keys**:
  - Cohere API key for embeddings.
  - OpenAI API key for generation.
  - (Optional) LangSmith API key for tracing.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Anas-github-acc/IntoxAI
cd IntoxAI
```

Install Poetry globally if not already installed:

### Step 2: Install Poetry

#### Pip Installtion

```bash
pip install -g poetry
```

#### or Curl Installation

Linux/Mac:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows (PowerShell):

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Verify installation:

```bash
poetry --version
```

Add Poetry to your PATH if needed (see Poetry docs).

### Step 3: Install Dependencies with Poetry

Poetry will install dependencies from pyproject.toml into a virtual environment.

Linux/Mac or Windows:

```bash
poetry install
```

This creates a virtual environment and installs all required packages (e.g., langchain, cohere, chromadb).

### Step 4: Set Up the .env File

Rename .env.template to .env:

Linux/Mac:

```bash
mv .env.template .env
```

Windows (Command Prompt):

```cmd
ren .env.template .env
```

Open .env in a text editor and add your API keys:

```bash
COHERE_API_KEY=your-cohere-api-key-here
OPENAI_API_KEY=your-openai-api-key-here
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your-langsmith-api-key-here
LANGSMITH_PROJECT=pr-yellowish-man-97
```

Replace your-cohere-api-key-here, your-openai-api-key-here, and your-langsmith-api-key-here with your actual API keys. Leave LangSmith variables unchanged if not using tracing.

### Step 5: Run the Project

Run the system using Poetry's script runner:

Linux/Mac:

```bash
poetry run start
```

Windows:

```bash
poetry run start
```

Alternatively, activate the Poetry shell and run directly:

Linux/Mac:

```bash
poetry shell
python main.py
```

Windows:

```bash
poetry shell
python main.py
```

You should see:

```bash
Ingesting documents...
Setting up RAG chain...
Welcome to the xAI FAQ RAG System! Ask a question (or type '/quit' or '/bye' to exit):
> 
```

## Usage

- Ask questions like "What is xAI's mission?" or "How does Grok work?"
- Type `quit` to exit.

## Troubleshooting	

- **Poetry Not Found**: Ensure Poetry is installed and in your PATH.
- **API Key Errors**: Verify .env contains valid keys.
- **Dependency Issues**: Run `poetry lock` then `poetry install` to resolve version conflicts.

## Notes

- The .env file is ignored by Git for security (see .gitignore).
- LangSmith tracing is optional; set LANGSMITH_TRACING=false in .env to disable it.
- Extend the FAQ by adding more content to data/faq.txt.

## Contribution

- Contributions are welcome! Please open an issue or pull request.
- For major changes, please open an issue first to discuss what you would like to change.
