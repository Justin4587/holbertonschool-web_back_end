#!/usr/bin/env python3
"""
    let the caching commence
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """somethings going to happen bets on Traceback??"""
    def put(self, key, item):
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key
