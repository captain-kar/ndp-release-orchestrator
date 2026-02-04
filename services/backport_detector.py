import os
import requests

GITHUB_API = os.getenv("GITHUB_API", "https://api.github.com")

def is_commit_in_branch(org, repo, branch, commit_sha, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    # Compare: branch...commit
    url = f"{GITHUB_API}/repos/{org}/{repo}/compare/{branch}...{commit_sha}"
    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        return False

    data = resp.json()

    # If status is "behind" or "diverged", commit not in branch
    return data.get("status") == "identical" or data.get("ahead_by", 1) == 0
