
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
import json
SystemPrompt = """
You are an expert AI assistant that solves problems step by step.

You must return ALL steps together as ONE valid JSON ARRAY.

Each item in the array must follow this format exactly:
{
  "step": "START" | "PLAN" | "OUTPUT",
  "content": "string"
}

Rules:
- Always return a SINGLE JSON ARRAY.
- Do NOT return multiple JSON objects separately.
- Do NOT add any text outside the JSON.
- The sequence must be: START → one or more PLAN → OUTPUT.
- The final answer must be only in the OUTPUT step.

Example:

User: Hey, can you solve 2 + 3 * 5 / 10

Output:
[
  {"step":"START", "content":"User wants to solve a mathematical expression."},
  {"step":"PLAN", "content":"We should apply the BODMAS rule."},
  {"step":"PLAN", "content":"First multiply 3 * 5 = 15."},
  {"step":"PLAN", "content":"Now divide 15 / 10 = 1.5."},
  {"step":"PLAN", "content":"Now add 2 + 1.5 = 3.5."},
  {"step":"OUTPUT", "content":"2 + 3 * 5 / 10 = 3.5"}
]
"""


print("\n\n\n")

message_history = [
    {"role": "system" , "content": SystemPrompt},
]

user_input = input("🫴 \t")

message_history.append({"role":"user" , "content":user_input})


llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434",
)



response = llm.invoke( message_history )

raw_result = (response.content)

 
message_history.append({"role" : "assistant" , "content": raw_result})
 
parsed_result = json.loads(raw_result)
# print("\n\n",parsed_result)

i =0

while True: 
 if parsed_result[i].get("step") == "START":
     print("🔥" , parsed_result[i].get("content"))
     
 elif parsed_result[i].get("step") == "PLAN":
     print("🧠" , parsed_result[i].get("content"))
     
 elif parsed_result[i].get("step") == "OUTPUT":
     print("🗣️" , parsed_result[i].get("content"))
     break
 i = i+1