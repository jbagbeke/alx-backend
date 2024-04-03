#!/usr/bin/env python3
"""
Least Recently Used (LRU) Caching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching system with Base Caching as Base class
    """

    def __init__(self):
        """
        Constructor method
        """
        super().__init__()
        self.least_access = {}
        self.lru_age = -1

    def put(self, key, item):
        """
        Stores Item in cache system
        """
        if key and item:
            self.cache_data[key] = item

            self.lru_age += 1
            self.least_access[key] = self.lru_age

            if len(self.cache_data) > super().MAX_ITEMS:
                least_key = min(self.least_access, key=self.least_access.get)

                del self.cache_data[least_key]
                del self.least_access[least_key]

                print('DISCARD: {}'.format(least_key))

    def get(self, key):
        """
        Returns Value of key specified
        """
        key_value = self.cache_data.get(key)

        if not key_value or not key:
            return None

        self.lru_age += 1
        self.least_access[key] = self.lru_age

        return key_value
