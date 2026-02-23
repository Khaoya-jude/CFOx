# app/memory/semantic.py
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

class SemanticMemory:
    def __init__(self, persist_dir="./vector_db"):
        self.db = Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())

    def remember(self, text: str, metadata: dict):
        self.db.add_texts([text], metadatas=[metadata])

    def recall(self, query: str, top_k=5):
        return self.db.similarity_search(query, k=top_k)

# Install the required packages
# !pip install langchain-community
# !pip install langchain-openai
