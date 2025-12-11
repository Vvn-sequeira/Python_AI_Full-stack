from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv() 

GEMENI_API=os.getenv("GEMENI_API")

client = OpenAI(
    api_key=GEMENI_API,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SystemPrompt = """"

You're an expert AI assistant in resolving user queries using chain of thought.
You work on start , plan and output steps.
You need to first Plan whaht needs to be done. the plan can be multiple steps.
Once you think enough Plan has been done, finally you can give an OUTPUT.

Rules: 
- Strictly follow the given JSON output format
- Only run one step at a time .
- The sequence of steps is START ( where User gives an input) , PLAN (that can be multiple times) and finally output (which is going to the displayed to the user)

OUTPUT JSON Fromat: 
{"Step":"START" | "PLAN" | "OUTPUT" , "content":"string" }

Example: 
START: Hey, can you solve 2 + 3 * 5 /10
PLAN: {"step":"START" : "content":"Seems like user is interested in maths prolem" }
PLAN: {"step": "PLAN" : "content": "looking at the problem , we should solve this using BODMAS method"}
PLAN: {"step": "PLAN" : "content": "first we must multiply 3*5 which is 15"}
PLAN: {"step": "PLAN" : "content": "Now the new equestion is 2 + 15/10"}
PLAN: {"step": "PLAN" : "content": " we must perform 15/10 = 1.5 "}
PLAN: {"step": "PLAN" : "content": " Now the new equestion is 2 + 1.5"}
PLAN: {"step": "PLAN" : "content": " we must perform 2+1.5 = 3.5 "}
PLAN: {"step": "PLAN" : "content": " Great, we have solved and the ans is 3.5 "}
PLAN: {"step": "OUTPUT" : "content": " 2 + 3 * 5 /10 = 3.5 "}


"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role": "system", "content":SystemPrompt},
        {
            "role": "user",
            "content": "write a code to calculat the seriese of a Prime No.  "
        }
        #keep adding msg to the history 

    ]
)

print(response.choices[0].message.content)