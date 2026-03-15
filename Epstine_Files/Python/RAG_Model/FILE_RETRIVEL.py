import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from qdrant_client import QdrantClient
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore 
from langchain_nomic import NomicEmbeddings

load_dotenv()




Qdrant_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_CLUSTER_END_POINT=os.getenv("QDRANT_CLUSTER_END_POINT")



def Vector_search(filename , user_query):
    

    embedding_model = NomicEmbeddings(
        model="nomic-embed-text-v1",
        nomic_api_key=os.getenv("NOMIC_API_KEY"),
    )
    
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=os.getenv("HF_TOKEN"),
    )
    
    print("I am here with 1", filename , "annd " , user_query)
    
    vecotr_store = QdrantVectorStore.from_existing_collection(
        embedding=embedding_model,
        # url="http://localhost:6333",
        url=QDRANT_CLUSTER_END_POINT,
        api_key=Qdrant_API_KEY,
        collection_name=f"{filename}"
    )
    
    SYS_PROMPT1=f"""
        Expand the user query with relevant keywords and synonyms to improve vector search accuracy.
        Return only the improved query as a single string. No extra text.

        Example:
        user_query: Did Johanna have a fight with anyone?
        improved_query: Did Johanna have any conflict, argument, dispute, or confrontation with any individual or group?

        user_query: Did Iran sexually harass underage girls?
        improved_query: Were there any incidents of sexual abuse, misconduct, exploitation, or assault on minors, underage females, or young girls in Iran, involving coercion, grooming, or inappropriate contact?

        user_query: {user_query}
    """
    
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct:together",
        messages=[
            {"role":"system" , "content":SYS_PROMPT1}
            ,{"role":"user" , "content":"Improve My query please"}
        ]
    )
   
    imporoved_user_query=completion.choices[0].message.content
    # user_query = input("What's your Question to JEFERYY EPSTINE>>>>")

    search_result = vecotr_store.similarity_search(query=imporoved_user_query)
    
    print("⚠️⚠️  Vectot search is DONE ") 
    # print(search_result[0])
    context=[
        f"Page Content: {result.page_content}"
        f"Page NUMBER: {result.metadata['page']}"
        f"Total Page: {result.metadata['total_pages']}"
        f"Source: Justice Department of USA"
        for result in search_result
    ]
    print("⚠️⚠️  Context is DONE ") 
    SYS_PROMPT=f"""
        You are the documents — a collection of files, reports, and records provided to you.
        Speak as the documents themselves, not as an AI.

        Answer only from the context provided. If context is insufficient, reference relevant 
        publicly known statements or reports, clearly stating the source.

        Never identify yourself as an AI or say "based on the document." 
        You ARE the document — speak from within it.

        Example:
        User: Is [person] involved?
        You: [Person] appears in... (continue with context)

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

    result = AiAgentReply(imporoved_user_query)
    # print(result)
    return result.content
 
        
# Vector_search("Epstine_Questioning_FILE","Did Johhana have sex with anyone? ")

