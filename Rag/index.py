from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = Path(__file__).parent / "PDFFORRAG.pdf"


# Load this file 
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load() 

print(docs[0])

# split the docs 

Text_spliiter =  RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = Text_spliiter.split_text(documents=docs)