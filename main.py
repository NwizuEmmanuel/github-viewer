import requests

url = 'https://api.quotable.io/random'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Quote: {data["quote"]}")
    print(f"Author: {data["author"]}")
else:
    print("Request has failed.")