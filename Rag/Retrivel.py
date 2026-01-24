from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


# Vector emmbedding
embeddinng_model= OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

vecotr_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddinng_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# User query
user_input = input("Ask something about the docs ")

# similarity check on the chunks stored in Vector DB
search_result = vecotr_store.similarity_search(query=user_input)
# print(search_result.page_content)
context = "\n\n".join([
    f"Page content: {result.page_content}\n"
    f"Page Number: {result.metadata['page_label']}\n"
    f"File Location: {result.metadata['source']}"
    for result in search_result
])

SYSTEM_PROMPT=f'''
You are a helpfull AI Assistent who answer user query based on the available context retreived from a PDF file along with page_contents and page number. 
You should only answer the user based on the following context and navigate the user to open the right page number to know more. 

Context: 
{context}
'''

llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434",
)

messages=[
    SystemMessage(content=SYSTEM_PROMPT),
    HumanMessage(content=user_input)      
]

response = llm.invoke(messages)

print("\n🤖 Answer:\n")
print(response.content)