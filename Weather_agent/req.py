import requests
from langchain_ollama import ChatOllama
import json 

# URL = "https://wttr.in/Delhi?format=%C+%t"

# res = requests.get(URL)

# print(res.status_code , "\n" , res.text) 

def printf ():
    print("hello world !")

available_tools = {
    'printTool' : printf 
}

available_tools['printTool']() 


# llm = ChatOllama(
#     model="qwen2.5:7b-instruct",
#     base_url="http://localhost:11434",
# )

# res = llm.invoke("Respond only in JSON: {\"hello\": \"world\"}")
# print(res.content)
# jsonres = json.loads(res.content)
# print(type(jsonres))
