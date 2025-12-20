from openai import OpenAI
from dotenv import load_dotenv
import os 
import requests 

load_dotenv() 

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
        

user_input = input("\n \n 👤=> \n\n")

def main(user_query):
 response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": user_query
        }
    ]
   )
 print("🤖",response.choices[0].message.content)


main(user_input)

