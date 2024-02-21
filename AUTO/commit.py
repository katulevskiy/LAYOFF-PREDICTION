import requests
import random

# GitHub credentials
username = "your_username"
token = "your_personal_access_token"

# List of repositories
repositories = ["repo1", "repo2", "repo3"]

# Generate random commit message
verbs = ["Added", "Modified", "Fixed", "Updated"]
nouns = ["feature", "bug", "code", "documentation"]
adjectives = ["awesome", "critical", "minor", "important"]
commit_message = (
    f"{random.choice(verbs)} {random.choice(adjectives)} {random.choice(nouns)}"
)

# Commit to repositories
for repo in repositories:
    url = f"https://api.github.com/repos/{username}/{repo}/git/commits"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "message": commit_message,
        "content": "bXkgbmV3IGZpbGUgY29udGVudHM=",
        # This content is just a placeholder, you might want to replace it with actual file content
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Commit created successfully in {repo}")
    else:
        print(f"Failed to create commit in {repo}: {response.text}")
