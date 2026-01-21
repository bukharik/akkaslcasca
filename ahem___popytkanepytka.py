import requests

url = "https://graph.threads.net/v1.0/keyword_search"

params = {
    "q": "kitties",
    "search_type": "TOP",
    "fields": (
        "id,text,media_type,permalink,timestamp,"
        "username,has_replies,is_quote_post,is_reply"
    ),
    "access_token": "ACCESS_TOKEN"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())