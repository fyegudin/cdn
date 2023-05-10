from abc import ABC, abstractmethod


class BaseCache(ABC):
    @abstractmethod
    def get(self, url: str) -> bytes:
        pass

    @abstractmethod
    def put(self, url: str, content: bytes) -> None:
        pass

    @abstractmethod
    def has(self, url: str) -> bool:
        pass
