import boto3
from .base_cache import BaseCache


class EC2Cache(BaseCache):
    def __init__(self, instance_id: str):
        self.instance_id = instance_id
        self.ec2 = boto3.client('ec2')

    def get(self, url: str):
        # implementation
        pass

    def put(self, url: str, content: bytes) -> None:
        # implementation
        pass

    def has(self, url: str) -> bool:
        # implementation
        pass

    def changed_storage(self, url: str):
        # implementation
        pass

    def changed_cpu(self, url: str):
        # implementation
        pass



