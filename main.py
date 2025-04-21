import requests

class Vyntr:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://vyntr.com/api"

    def search(self, query : str):
        url = f"{self.base_url}/search?q={query}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response
