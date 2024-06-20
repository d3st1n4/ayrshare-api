import requests
import json

AYRSHARE_API_KEY = os.environ.get("AYRSHARE_API_KEY")

payload = {
  "post": "Today is a great day!",
  "platforms": ["twitter"],
  "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"],
}
      
# Live API Key
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {AYRSHARE_API_KEY}'
}

url = 'https://app.ayrshare.com/api/post'
      
r = requests.post(url, json=payload, headers=headers) 

if r.status_code == 200:
    print("Post successfully made.")
    response = r.json()
    print(response)  # If needed, print the response JSON
else:
    print(f"Failed to post: {r.status_code}")
    error_json = r.json()
    print(error_json)




