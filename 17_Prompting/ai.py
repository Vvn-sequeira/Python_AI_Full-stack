import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMENI_API")  # make sure env name matches
model = "gemini-2.5-flash"

url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"

message = "Hello Gemini!"

payload = {
    "contents": [
        {
            "parts": [
                {"text": message}
            ]
        }
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    headers=headers,
    data=json.dumps(payload)
)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
