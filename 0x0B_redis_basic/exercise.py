"""something about redis"""
import redis
from uuid import uuid4
from typing import Union


class Cache():
    """Cache class for redis module"""

    def __init__(self):
        """something about redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """something about redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
