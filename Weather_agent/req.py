import requests
from langchain_ollama import ChatOllama
import json 

<<<<<<< HEAD
# URL = "https://wttr.in/Delhi?format=%C+%t"
=======
URL = "https://wttr.in/Delhi?format=%C+%t"
>>>>>>> f1dc9fa86f3e00a1aa505f84bd1db71015a06781

# res = requests.get(URL)

<<<<<<< HEAD
# print(res.status_code , "\n" , res.text) 

def printf ():
    print("hello world !")

available_tools = {
    'printTool' : printf 
}

available_tools['printTool']() 
=======
print(res.status_code , "\n" , res.text) 


>>>>>>> f1dc9fa86f3e00a1aa505f84bd1db71015a06781


# llm = ChatOllama(
#     model="qwen2.5:7b-instruct",
#     base_url="http://localhost:11434",
# )

# res = llm.invoke("Respond only in JSON: {\"hello\": \"world\"}")
# print(res.content)
# jsonres = json.loads(res.content)
# print(type(jsonres))
