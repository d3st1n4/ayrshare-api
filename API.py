import requests
import json
import sqlalchemy as db
import pandas as pd
import os

AYRSHARE_API_KEY = os.environ.get("AYRSHARE_API_KEY")

# GET request
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {AYRSHARE_API_KEY}'
}

url_accounts = 'https://app.ayrshare.com/api/accounts'

r = requests.get(url_accounts, headers=headers)

if r.status_code == 200:
    print("Account successfully retrived.")
    response = r.json()
    print(response)
else:
    print(f"Failed to retrieve account: {r.status_code}")
    error_json = r.json()
    print(error_json)


# POST request
payload = {
  "post": "Today is a great day!",
  "platforms": ["twitter"],
  "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"],
}

url_posts = 'https://app.ayrshare.com/api/post'

r = requests.post(url_posts, json=payload, headers=headers)

if r.status_code == 200:
    print("Post successfully made.")
    response = r.json()
    print(response)  
else:
    print(f"Failed to post: {r.status_code}")
    error_json = r.json()
    print(error_json)

data_dict = {
  "post": "Today is a great day!",
  "platforms": ["twitter"],
  "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"]
}

dataframe = pd.DataFrame.from_dict(data_dict)
engine = db.create_engine('sqlite:///data_base_name.db')
dataframe.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute
    (db.text("SELECT * FROM table_name;")).fetchall()
    print(pd.DataFrame(query_result))
