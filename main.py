import requests
import json

def show_activity(data):
    counter = 1
    for item in data[:20]:
        type = item['type']
        created_at = item['created_at']
        repo = item['repo']['name']

        if "commits" in item['payload']:
            count_commits = len(item['payload']['commits'])
        print(f"{counter}. type: {type}, created_at: {created_at}, repo: {repo}, commits: {count_commits or 0}")
        count_commits = 0
        counter += 1

def main():
    username = "NwizuEmmanuel"
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        show_activity(data=data)
    else:
        print("Request has failed.")

if __name__ == "__main__":
    main()