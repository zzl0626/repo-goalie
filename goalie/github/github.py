import requests

class GitHubClient:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"

    def _headers(self):
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }

    def get_user(self):
        url = f"{self.base_url}/user"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_repository(self, owner: str, repo: str):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def create_pull_request(
        self, owner: str, repo: str, title: str, body: str, head: str, base: str
    ):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        data = {"title": title, "body": body, "head": head, "base": base}
        response = requests.post(url, headers=self._headers(), json=data)
        response.raise_for_status()
        return response.json()
    
    def get_repository_from_actions(self, owner: str, repo: str):
        # get repository from github actions
        url = f"{self.base_url}/repos/{owner}/{repo}/actions"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()
    
    def get_repository_from_local(self, owner: str, repo: str):
        # get repository from local
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()
    
    def list_pull_requests(self, owner: str, repo: str, state: str = "open"):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls?state={state}"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def list_repositories(self, user: str):
        url = f"{self.base_url}/users/{user}/repos"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

