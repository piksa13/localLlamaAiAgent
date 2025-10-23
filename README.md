# localLlamaAiAgent with RAG

localLlamaAiAgent is a **RAG** Retrieval-Augmented Generation(combines language model & external knowledge) that uses the LangChain framework, Ollama and Chroma DB to build AI agents capable of local language model inference and data processing.

## Features

- **LangChain Integration:** Modular framework for building language model-powered applications.
- **Ollama Support:** Enables running and managing local Llama models.
- **Chroma Vector Store:** Efficient storage and retrieval of embeddings for semantic search.
- **Data Analysis:** Uses pandas for data manipulation and analysis.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/localLlamaAiAgent.git
cd localLlamaAiAgent
pip install -r requirements.txt
```

## Requirements

- Ollama with local model e.g. mxbai-embed-large
- Python 3.x
- See `requirements.txt` for package details:
  - langchain
  - langchain-ollama
  - langchain-chroma
  - pandas

## Usage

Customize and extend the agent logic in your Python scripts to interact with local Llama models and process data.
