import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore 


load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

embeddinng_model= OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

vecotr_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddinng_model,
    url="http://localhost:6333",
    collection_name="Epstine_Questioning_FILE"
)

user_query = input("What's your Question to JEFERYY EPSTINE>>>>")

search_result = vecotr_store.similarity_search(query=user_query)
# print(search_result[0])
context=[
    f"Page Content: {result.page_content}"
    f"Page NUMBER: {result.metadata['page']}"
    f"Total Page: {result.metadata['total_pages']}"
    f"Source: Justice Department of USA"
    for result in search_result
]

SYS_PROMPT=f"""
You are an helpfull AI assistent , helping user to go through the EPSTIEN FILES.
Answer UserQuery based on the Context provided to you.

NOTE: DON"T Answer anything outside the Context Provided to you but you can answer the user query if the context is not enough for answering the question , you can mention like " according to the news report and FBI statement this and that . 



CONTEXT: {context}
"""

def AiAgentReply(query:str):
    print(f"the query users sent is : {query}")
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct:together",
        messages=[
            {"role":"system" , "content":SYS_PROMPT},
            {"role": "user" , "content": query}
        ],
      
    )
    
    message = completion.choices[0].message
    return message

result = AiAgentReply(user_query)
print(result)
 
        
