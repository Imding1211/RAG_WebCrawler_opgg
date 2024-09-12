
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from query_controller import query_rag
from langchain_chroma import Chroma

LLM_MODEL_NAME = "gemma2:2b"
LLM_MODEL      = Ollama(model=LLM_MODEL_NAME)

EMBEDDING_MODEL_NAME = "all-minilm"
EMBEDDING_MODEL      = OllamaEmbeddings(model=EMBEDDING_MODEL_NAME)

CHROMA_PATH    = "chroma"

DATABASE = Chroma(
    persist_directory  = CHROMA_PATH, 
    embedding_function = EMBEDDING_MODEL
    )


PROMPT_TEMPLATE = """
{context}

---

根據以上資料用繁體中文回答問題: {question}
"""

def run():
    while True:
        query_text = input("輸入問題或 exit 停止:\n")

        if query_text == "exit":
            break

        response = query_rag(query_text, 2, LLM_MODEL, PROMPT_TEMPLATE, DATABASE)
        print(response)
        print("\n")
        
        
if __name__ == "__main__":
    run()
    
    