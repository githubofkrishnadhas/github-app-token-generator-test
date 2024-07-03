import requests
import os
import argparse
from dotenv import load_dotenv


def create_github_label(repo:str, label_name:str):
    url = f"https://api.github.com/repos/{repo}/labels"
    headers = {
        "Authorization": f"token {os.getenv('GH_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "name": label_name,
        "color": "f29513",  # Default color for the label, you can change this
        "description": f"Label {label_name}"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Label '{label_name}' created successfully in repository '{repo}'!")
    else:
        print(f"Failed to create label '{label_name}' in repository '{repo}'.")
        print("Response:", response.json())


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Create a GitHub label in a repository.')
    parser.add_argument('--repo', type=str, help='GitHub repository name in the format "owner/repo".')
    parser.add_argument('--label_name', type=str, help='Name of the label to create.')

    args = parser.parse_args()
    repo = args.repo
    label_name = args.label_name
    # Get the GitHub token from environment variable or argument
    # github_token = os.getenv('GITHUB_TOKEN')

    create_github_label(repo=repo, label_name=label_name)
