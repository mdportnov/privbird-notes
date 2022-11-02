from .rule import Rule

BRUTE_FORCE_REDIS_HOST = 'redis'
BRUTE_FORCE_REDIS_PORT = 6379
BRUTE_FORCE_REDIS_DB = 0
BRUTE_FORCE_LIMITS = {'default': Rule(IP = 10)}
BRUTE_FORCE_TIME_LIMIT = 60