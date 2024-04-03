#!/usr/bin/env python3
"""
Most Recently Used (MRU) Caching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Caching system with Base Caching as Base class
    """

    def __init__(self):
        """
        Constructor method
        """
        super().__init__()
        self.most_accessed = {}
        self.mru_age = -1

    def put(self, key, item):
        """
        Stores Item in cache system
        """
        if key and item:
            self.cache_data[key] = item

            self.mru_age += 1
            self.most_accessed[key] = self.mru_age

            if len(self.cache_data) > super().MAX_ITEMS:
                most_value = max(self.most_accessed.values())
                most_key = [key for key, val in self.most_accessed.items()
                             if val == most_value][0]

                del self.cache_data[most_key]
                del self.most_accessed[most_key]

                print('DISCARD: {}'.format(most_key))

    def get(self, key):
        """
        Returns Value of key specified
        """
        key_value = self.cache_data.get(key)

        if not key_value or not key:
            return None

        self.mru_age += 1
        self.most_accessed[key] = self.mru_age

        return key_value