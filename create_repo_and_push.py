import requests
import os
import subprocess

class GitHub_API:
    def __init__(self, access_token):
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def create_repo(self, repo_name):
        data = {
            "name": repo_name,
            "description": "Initial Repo Commit",
            "homepage": "https://github.com",
            "private": True,
            "is_template": True
        }
        response = requests.post('https://api.github.com/user/repos', headers=self.headers, json=data)
        return response

    def initialize_git_repo(self):
        local_repo_path = os.getcwd()
        print("Local Repository Path:", local_repo_path)
        os.makedirs(local_repo_path, exist_ok=True)
        os.chdir(local_repo_path)
        subprocess.run(["git", "init"])


    def push_to_github(self, commit_message="update", repo_name="heroku_flask_safeum_test"):
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", commit_message])
        remote_repo = "https://github.com/melodic456/" + str(repo_name) + ".git"
        subprocess.run(["git", "remote", "add", "origin", remote_repo])
        subprocess.run(["git", "push", "-u", "origin", "master"])
        subprocess.run(["git", "push"])

# Example usage
access_token = "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"
repo_name = "heroku-novnc-ext2"
github = GitHub_API(access_token)
# Create a repository
response = github.create_repo(repo_name)
if response.status_code == 201:
    print("Repository created successfully")
# Initialize Git repository
    github.initialize_git_repo()
# Push to GitHub with a custom commit message
github.push_to_github(repo_name=repo_name)
