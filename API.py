import requests
import json
import sqlalchemy as db
import pandas as pd
import os

AYRSHARE_API_KEY = os.environ.get("AYRSHARE_API_KEY")

# GET request
# Normal case: valid api key
# Edge case: invalid api key, no api key
def get_account_info(api_key):
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {api_key}'
    }
    url_accounts = 'https://app.ayrshare.com/api/accounts'
    response = requests.get(url_accounts, headers=headers)
    return response

# POST request
# Normal case: valid api key and payload
# Edge case: invalid api key and payload, no api key and/or payload 
def post_tweet(api_key, payload):
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {api_key}'
    }
    url_posts = 'https://app.ayrshare.com/api/post'
    response = requests.post(url_posts, json=payload, headers=headers)
    return response

# Normal case: valid data_dict, db_name and table_name
# Edge case: invalid data_dict, db_name and table_name, 
# no data_dict, db_name, and/or table_name
def save_to_database(data_dict, db_name, table_name):
    engine = db.create_engine(f'sqlite:///{db_name}.db')
    dataframe.to_sql(table_name, con=engine, if_exists='replace', index=False)
    with engine.connect() as connection:
        query_result = connection.execute(db.text(f"SELECT * FROM {table_name};")).fetchall()
    return pd.DataFrame(query_result)

if __name__ == "__main__":
    account_response = get_account_info(AYRSHARE_API_KEY)
    if r.status_code == 200:
        print("Account successfully retrived.")
        print(account_response.json())
    else:
        print(f"Failed to retrieve account: {account_response.status_code}")
        print(account_response.json())

    tweet_payload = {
    "post": "Today is a great day!",
    "platforms": ["twitter"],
    "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"]
    }
    post_response = post_tweet(AYRSHARE_API_KEY, tweet_payload)
    if post_response.status_code == 200:
        print("Post successfully made.")
        print(post_response.json())
    else:
        print(f"Failed to post: {post_response.status_code}")
        print(post_response.json())

    save_result = save_to_database(tweet_payload, 'data_base_name', 'table_name')
    print(save_result)


