
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma
from bs4 import BeautifulSoup
import requests

EMBEDDING_MODEL_NAME = "all-minilm"

CHROMA_PATH     = "chroma"
EMBEDDING_MODEL = OllamaEmbeddings(model=EMBEDDING_MODEL_NAME)

DATABASE = Chroma(
    persist_directory  = CHROMA_PATH, 
    embedding_function = EMBEDDING_MODEL
    )

URL="https://www.op.gg/champions"

resp=requests.get(URL)

soup = BeautifulSoup(resp.text,"html5lib") 

champions = soup.find('table', class_='css-f65xnu egex0vq1').find_all('strong')

champions_document = []
champions_ids = []

for index, champion in enumerate(champions[0:10]):
    
    document = Document(page_content=f'Rank:{index+1},Champion:{champion.getText()}')
    
    champions_document.append(document)
    
    champions_ids.append(f'ids_{index+1}')
    
DATABASE.add_documents(champions_document, ids=champions_ids)

data = DATABASE.get()

print("Done !!")