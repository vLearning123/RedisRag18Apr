import redis

def get_redis_client():
    """
    Create and return a Redis client instance.
    """
    return redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        # decode_responses=True
    )