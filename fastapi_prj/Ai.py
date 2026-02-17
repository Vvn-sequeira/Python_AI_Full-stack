import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from fastapi import FastAPI

app = FastAPI() 

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather of a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_Menu",
            "description":"Get the Menu List",
            "parameters":"none"
        }
    }
]

def get_Menu():
    return f"Menu: chai , tea , dosa , idli , chapathi , juice , mango , sarbath "


def AiAgentReply(query:str):
    print(f"the query users sent is : {query}")
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct:together",
        messages=[
            {"role": "user" , "content": query}
        ],
        tools=tools
    )
    
    message = completion.choices[0].message
    print(message)
    if message.tool_calls[0].function.name == "get_Menu":
        print(message.content or " " + "  \n "+get_Menu())
        return message.content or " " +"  \n "+get_Menu()
        





    
