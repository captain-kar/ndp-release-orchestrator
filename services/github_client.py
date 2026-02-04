import os
import requests

GITHUB_API = "https://api.github.com"


def get_merged_prs(org, repo, base_branch, limit=10):
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    url = f"{GITHUB_API}/repos/{org}/{repo}/pulls"
    params = {
        "state": "closed",
        "base": base_branch,
        "per_page": limit
    }

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()

    prs = []
    for pr in resp.json():
        if pr.get("merged_at"):
            prs.append({
                "number": pr["number"],
                "title": pr["title"],
                "url": pr["html_url"],
                "merged_at": pr["merged_at"],
                "merge_commit_sha": pr["merge_commit_sha"]
            })

    return prs
