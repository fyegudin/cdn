from cdn.components.clients.base_client import BaseClient


class Client(BaseClient):
    def __init__(self, router_url):
        super().__init__(router_url)

    # Additional methods for the Client class can be added here
