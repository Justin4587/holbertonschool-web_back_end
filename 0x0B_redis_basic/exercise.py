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


def call_history(method: Callable) -> Callable:
    """something about redis"""
    in_ = f"{method.__qualname__}:inputs"
    out_ = f"{method.__qualname__}:outputs"

    @wraps(method)
    def call_history_wrap(self, *args) -> bytes:
        """something about redis"""
        self._redis.rpush(in_, str(args))
        output = method(self, *args)
        self._redis.rpush(out_, output)
        return output
    return call_history_wrap


def replay(method: Callable):
    """something about redis"""
    _self = method.__self__
    q_name = method.__qualname__
    calls = _self.get(q_name)

    if calls:
        num = _self.get_str(calls)
        ins = _self._redis.lrange(calls + ":inputs", 0, -1)
        outs = _self._redis.lrange(calls + ":outputs", 0, -1)
    print(f"{calls} was called {num} times:")
    zip_val = zip(ins, outs)
    result = list(zip_val)
    for k, v in result:
        name = _self.get_str(k)
        number = _self.get_str(v)
        print(f"{calls}(*{name}) -> {number}")


class Cache():
    """Cache class for redis module"""

    def __init__(self):
        """something about redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
