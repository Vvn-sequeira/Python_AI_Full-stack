from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader 
from pathlib import Path 
from dotenv import load_dotenv
import os 
load_dotenv() 

Qdrant_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_CLUSTER_END_POINT=os.getenv("QDRANT_CLUSTER_END_POINT")


pdf_path = Path(__file__).parent / "JEF_Questioning_FILE.pdf"
print("YES! Got the Path of the PDF")

PDFLoader = PyPDFLoader(pdf_path)
docs = PDFLoader.load()
print("YES! PDF Loaded")

Text_Splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400 
)
Chunks = Text_Splitter.split_documents(docs)
print("YES! Done Creating Chunks")

#Embedd
embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"   
)

#Store it in vector DB
vector_search = QdrantVectorStore.from_documents(
    documents=Chunks,
    embedding=embedding,
    # url="http://localhost:6333",
     url=QDRANT_CLUSTER_END_POINT, 
     api_key=Qdrant_API_KEY,
     collection_name="Epstine_Court_Questioning_FILE"
)
print("Done storing the Vector embedded Data to the cloud")
print("*****************DONE************************")

#from qdrant_client import QdrantClient

# qdrant_client = QdrantClient(
#     url="https://c368fe9f-84b0-429a-9536-904cd1f6ebb1.europe-west3-0.gcp.cloud.qdrant.io:6333", 
#     api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.3YIDOGidszycGxkWuj86s7hl5DImHkQ7gu509vKdMd4",
# )

# print(qdrant_client.get_collections())