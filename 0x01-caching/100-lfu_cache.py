#!/usr/bin/python3
""" LFU Caching"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache system"""
    def __init__(self):
        """"""
        super().__init__()
        self.cache_data = {}
        self.lfu = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            lfu_key = self.lfu.pop(0)
            del self.cache_data[lfu_key]
            print("DISCARD: {}".format(lfu_key))
        self.cache_data[key] = item
        if key in self.lfu:
            self.lfu.remove(key)
        self.lfu.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.lfu.remove(key)
        self.lfu.append(key)
        return self.cache_data[key]