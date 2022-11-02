from ipware.ip import get_client_ip

from .settings import *


class Checker:
    name = 'IP'
    key_template = '{rule}:{checker}:{value}:int'
    
    def __init__(self, connection, request, load_count, **kwargs):
        self.connection = connection
        self.load_count = load_count
        self.key = self.get_key(request, **kwargs)
        self.limit = getattr(BRUTE_FORCE_LIMITS['default'], self.name)
    
    def get_key(self, request, **kwargs):
        return self.key_template.format(
            rule = 'default',
            checker = self.name,
            value = get_client_ip(request),
        )
    
    def get_load_count(self):
        data = self.connection.get(self.key)
        if not data:
            return 0
        
        ttl = self.connection.ttl(self.key)
        if ttl < 0:
            self.connection.delete(self.key)
            return 0
        
        return int(data)
    
    def update(self):
        if self.connection.exists(self.key):
            self.connection.incr(self.key, 1)
        else:
            self.connection.set(self.key, 1)
            self.connection.expire(self.key, self.load_count * BRUTE_FORCE_TIME_LIMIT)
    
    def check(self):
        return self.get_load_count() < self.limit
    
    @classmethod
    def clear(cls, connection, rule = '*', value = '*'):
        template = cls.key_template.format(
            rule = rule,
            checker = cls.name,
            value = value,
        )
        
        for key in connection.keys(template):
            connection.delete(key)