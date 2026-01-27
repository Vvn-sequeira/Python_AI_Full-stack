import requests
import json
from langchain_ollama import ChatOllama

<<<<<<< HEAD
def weather(city: str):
    print("🌹 Weather function triggered with city name ", city )
    # URL = f"https://wttr.in/{city.lower()}?format=%C+%t"
   
    # res = await requests.get(URL)
    # print("👤", res )

    # if res.status_code == 200:
    #     return f"The weather in {city} is {res.text.strip()}"

    return f"weather in {city} is sunny with 40 deg  "
=======

async def  weather(city: str):
    URL = f"https://wttr.in/{city.lower()}?format=%C+%t"
    print("🌹 Weather function triggered with city name ", city )
    res = await requests.get(URL)
    print("👤", res )

    if res.status_code == 200:
        return f"The weather in {city} is {res.text.strip()}"

    return "Something went wrong, please try again later."
>>>>>>> f1dc9fa86f3e00a1aa505f84bd1db71015a06781

available_tools = {
    "weather": weather
}


SystemPrompt = """
You are an AI agent that follows a strict step-by-step reasoning and tool-usage protocol.

You MUST ALWAYS respond with EXACTLY ONE valid JSON object.
Do NOT return multiple JSON objects.
Do NOT write anything outside JSON.
Do NOT explain in plain text.

JSON Schema:
{
  "step": "START | PLAN | TOOL | OUTPUT",
  "content": "string",
  "tool": "string",
  "input": "string"
}

Rules:
1. Only ONE step per response.
2. First respond with step = START.
3. Then respond with one or more PLAN steps as needed.
4. If a tool is required, respond with step = TOOL and fill both "tool" and "input".
5. After the tool result is provided, continue with PLAN or go directly to OUTPUT.
6. Finally, respond with step = OUTPUT to answer the user.
<<<<<<< HEAD
7. Must wait for the Result from tool calling 
=======
>>>>>>> f1dc9fa86f3e00a1aa505f84bd1db71015a06781

Tool Rules:
- Available tool: weather(city: string)
- When calling the TOOL, ONLY return:
  {
    "step": "TOOL",
    "content": "Calling weather tool",
    "tool": "weather",
    "input": "<city>"
  }


Example:
First Loop: 
{"step": "START" , content: "User is asking for the weather in Mumbai" }
Second Loop: 
{"step": "PLAN" , content: "I need to call a tool for the city <Mumbai> " }
Third Loop: 
{"step": "PLAN" , content: "I do have tool called 'weather' in available tool , let me call the function for the city <Mumbai>  " }
Fourth Loop: 
{"step": "TOOL" , content: "I do have tool called 'weather' in available tool , let me call the function for the city <Mumbai>  " }
Fivth Loop: 
{"step": "TOOL" , content: "Calling weather tool for the city <Mumbai>  " , "tool" : "weather" , "input": "Mumbai" }
sixth Loop: 
{"step": "PLAN" , content: "I recived a result for the city Mumbai  " }
Seventh Loop: 
{"step": "OUTPUT" , content: "the weather in Mumbai is slightly cloudy with 29 deg temp " }


<<<<<<< HEAD

NOTE: 
If you violate this protocol, you have FAILED the task.

=======
NOTE: 
If you violate this protocol, you have FAILED the task.
>>>>>>> f1dc9fa86f3e00a1aa505f84bd1db71015a06781
"""


message_history = [
    {"role": "system", "content": SystemPrompt}
]

user_input = input("🫴 ")
message_history.append({"role": "user", "content": user_input})

llm = ChatOllama(
    model="qwen2.5:7b-instruct",
    base_url="http://localhost:11434",
)


while True:
    response = llm.invoke(message_history)
    raw_result = response.content.strip()


    if not raw_result:
        print("⚠️ Empty response, retrying...")
        continue

    try:
        parsed = json.loads(raw_result)
    except Exception as e:
<<<<<<< HEAD
=======
        print("❌ JSON ERROR:", e)
>>>>>>> f1dc9fa86f3e00a1aa505f84bd1db71015a06781
        break

    step = parsed.get("step")

    message_history.append({"role": "assistant", "content": raw_result})

    if step == "START":
        print("🔥", parsed["content"])

        message_history.append({
            "role": "user",
            "content": "Continue to the next step."
        })
        continue

    if step == "PLAN":
        print("🧠", parsed["content"])

        message_history.append({
            "role": "user",
            "content": "Continue to the next step."
        })
        continue

    if step == "TOOL":
        tool_name = parsed.get("tool")
        tool_input = parsed.get("input")
<<<<<<< HEAD
        print(f"🔪 CALLING TOOL: {tool_name}({tool_input})")
        result =  available_tools[tool_name](tool_input)
        print(f"🔪 TOOL RESULT:", result)
        message_history.append({
            "role": "assistant",
            "content": f"Tool result: {result}"
        })
=======

        print(f"🔪 CALLING TOOL: {tool_name}({tool_input})")

        result = available_tools[tool_name](tool_input)

        print(f"🔪 TOOL RESULT:", result)

        message_history.append({
            "role": "user",
            "content": f"Tool result: {result}"
        })

>>>>>>> f1dc9fa86f3e00a1aa505f84bd1db71015a06781
        continue

    if step == "OUTPUT":
        print("🗣️ FINAL:", parsed["content"])
        break
