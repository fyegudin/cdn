from .base_cache import BaseCache


class PhysicalCache(BaseCache):
    def __init__(self, ip_address: str):
        self.ip_address = ip_address

    def get(self, url: str):
        # implementation
        pass

    def put(self, url: str, content: bytes) -> None:
        # implementation
        pass

    def has(self, url: str) -> bool:
        # implementation
        pass
