from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore 
from langchain_ollama import OllamaEmbeddings

pdf_path = Path(__file__).parent / "PDFFORRAG.pdf"

# Load this file 
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load() 
# print(docs[0])

# split the docs 
Text_spliiter =  RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)
chunks = Text_spliiter.split_documents(docs)

#Vector emmbedding 
embeddinng_model= OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

vecotr_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddinng_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("Inndexing of doc DONE")