#!/usr/bin/env python3
"""something about redis"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """something about redis"""
    @wraps(method)
    def count_calls_wrap(self, *args) -> bytes:
        """something about redis"""
        self._redis.incr(method.__qualname__)
        return method(self, *args)
    return count_calls_wrap


class Cache():
    """Cache class for redis module"""

    def __init__(self):
        """something about redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """something about redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int,
                                                          float]:
        """somethings going to happen bets on Traceback??"""
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """something about redis"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """something about redis"""
        return self.get(key, int)
