import requests
import argparse
import json

def show_activity(data):
    counter = 1
    for item in data[:20]:
        type = item['type']
        created_at = item['created_at']
        repo = item['repo']['name']
        print(f"{counter}. type: {type}, created_at: {created_at}, repo: {repo}")
        count_commits = 0
        counter += 1

def main():
    parser = argparse.ArgumentParser(description="Github activity viewer.")
    parser.add_argument('name', type=str, help="Enter username")
    args = parser.parse_args()

    username = args.name
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        show_activity(data=data)
    else:
        print("Request has failed.")

if __name__ == "__main__":
    main()