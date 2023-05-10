import requests


class BaseClient:
    def __init__(self, router_url, client_id):
        self.router_url = router_url
        self.client_id = client_id

    def get_content(self, content_id):
        response = requests.get(f"{self.router_url}/content/{content_id}")
        if response.status_code == 302:
            redirect_url = response.headers['location']
            response = requests.get(redirect_url)
        return response.content

    def start(self):
        pass

    def exit(self):
        pass
