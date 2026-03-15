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


pdf_path = Path(__file__).parent / "PDF_Iran.pdf"
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
     collection_name="PDF_Iran"
)

print("Done storing the Vector embedded Data to the cloud")
print("*****************DONE************************")


# FILES NAME
# Sexual_Harasment_in_Iran.pdf
# PDF_Iran.pdf


