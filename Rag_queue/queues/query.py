from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

embeddinng_model= OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
    )

llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434",
    )

def get_result(query:str):

    vecotr_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddinng_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
    )
    search_result = vecotr_store.similarity_search(query=query)
    
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
    

    
    messages=[
    SystemMessage(content=SYSTEM_PROMPT),
    HumanMessage(content=query)      
    ]
    
    response = llm.invoke(messages)
    
    print("\n🤖 Answer:\n")
    print(response.content)
    
    
    return response.content





