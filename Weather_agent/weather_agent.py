from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
import os 
from fastapi import FastAPI , Body
from ollama import Client
load_dotenv() 
app = FastAPI() 

client = Client(
     host="http://127.0.0.1:11434"
)

GEMENI_API=os.getenv("GEMENI_API")

client = OpenAI(
    api_key=GEMENI_API,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def weather(city:str):
    URL = "https://wttr.in/{city.lower()}?format=%C+%t"
    res = requests.get(URL)
    
    if res.status_code == 200:
        return f"The weather in {city} is {res.text}"
    
    return f"Somehting went wrong !! , Please Try again Later ...."
   
available_tools = {
    "weather" : weather
}

SystemPrompt = """"

You're an expert AI assistant in resolving user queries using chain of thought.
You work on start , plan , TOOL and output steps.
You need to first Plan whaht needs to be done. the plan can be multiple steps.
Once you think enough Plan has been done, finally you can give an OUTPUT.
You can also use Availabe Tools to finish the user query .
for every tool you call , wait for the OBSERVE step and then proceed 

Rules: 
- Strictly follow the given JSON output format
- Only run one step at a time .
- The sequence of steps is START ( where User gives an input) , PLAN (that can be multiple times), TOOL(if user is asking somehting that needs to be resolved by using TOOLs) and finally output (which is going to the displayed to the user)

OUTPUT JSON Fromat: 
{"Step":"START" | "PLAN" | "TOOL" | "OUTPUT" | "OBSERVE" , "content":"string" , "input": "String" , "tool" : "string" , "output":"string"}

Available tools:
- weather(City: str) : which gives takes an string as an input and provide the output 

Example: 
 START: Hey, What is the current weather of Delhi
 PLAN: {"step":"START" : "content":"Seems like user is interested in Weather of Delhi" }
 PLAN: {"step": "PLAN" : "content": "looking at the user query , we should solve this by using available tool"}
 PLAN: {"step": "PLAN" : "content": "first we must use the available tool"}
 PLAN: {"step": "PLAN" : "content": "Great we have weather(City:str) available in tool"}
 PLAN: {"step": "PLAN" : "content": "Let me call it for the city Delhi as an input for the available tool weather(City:str)"} 
 PLAN: {"step": "OBSERVE" : "TOOL": "tool": "weather" , "input": "Delhi" , "output" : "the weather of Delhi is cloudy with 28 deg celcius }
 PLAN: {"step": "PLAN" : "content": "Great i got a output "} 
 OUTPUT: {"step": "OUTPUT" : "content": "the weather of Delhi is 28 C with cloudy sky "}


"""

print("\n\n\n")

message_history = [
    {"role": "system" , "content": SystemPrompt},
]

user_input = input("🫴")

message_history.append({"role":"user" , "content":user_input})

while True: 
 response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages= message_history

)
#  response= client.chat(model="gemma:2b" , messages=[
#         {"role" : "user" , "content": message_history }
        
#     ]) 
#  print(response.choices[0].message.content)
 
 raw_result = (response.choices[0].message.content)
 message_history.append({"role" : "assistant" , "content": raw_result})
 
 parsed_result = json.loads(raw_result)
 print(parsed_result)
 
 if parsed_result.get("step") == "START":
     print("🔥" , parsed_result.get("content"))
     continue
 if parsed_result.get("step") == "PLAN":
     print("🧠" , parsed_result.get("content"))
     continue
 if parsed_result.get("step") == "TOOL":
     tool_to_call = parsed_result.get("tool")
     tool_input = parsed_result.get("input")
     print(f"🔪: {tool_to_call} ({tool_input})" )
     
     res =  available_tools[tool_to_call](tool_input)
     print(f"🔪: {tool_to_call} ({tool_input}) = {res}" )     
     
     message_history.append({"role":"developer"  , "content": json.dumps({
         "step" : "OBSERVE"  , "tool" : tool_to_call , "input" : tool_input , "output": res
     })})
     
     continue
 if parsed_result.get("step") == "OUTPUT":
     print("🗣️" , parsed_result.get("content"))
     continue
 
