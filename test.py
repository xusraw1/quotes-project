import requests

response = requests.get("https://api.quotable.io/quotes?page=1").json()['results'][:5]
print(response)
