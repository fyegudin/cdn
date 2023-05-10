from .ec2_cache import EC2Cache


class CacheFactory:
    @staticmethod
    def create(cache_type: str, **kwargs):
        if cache_type == 'ec2':
            instance_id = kwargs.get('instance_id')
            if instance_id is None:
                raise ValueError('EC2 instance ID is missing')
            return EC2Cache(instance_id)
        elif cache_type == 'physical':
            ip_address = kwargs.get
