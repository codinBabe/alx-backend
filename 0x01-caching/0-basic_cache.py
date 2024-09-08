#!/usr/bin/python3
"""A basic cache implementation"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache implementation"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add data to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve data from cache based on the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
