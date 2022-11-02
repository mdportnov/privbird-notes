from redis import StrictRedis

from .checker import Checker
from .settings import *


class Attempt:
    connection = StrictRedis(
        host = BRUTE_FORCE_REDIS_HOST,
        port = BRUTE_FORCE_REDIS_PORT,
        db = BRUTE_FORCE_REDIS_DB,
    )
    
    error = 'Too many requests from this IP!'
    
    def __init__(self, request, load_count, **kwargs):
        self.checker = Checker(self.connection, request, load_count, **kwargs)
    
    def check(self):
        if not self.checker.check():
            return False
        
        self.checker.update()
        return True