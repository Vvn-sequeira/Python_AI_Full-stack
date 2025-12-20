import requests

URL = "https://wttr.in/{Mangalore}?format=%C+%t"

res = requests.get(URL)

print(res.status_code , "\n" , res.text)