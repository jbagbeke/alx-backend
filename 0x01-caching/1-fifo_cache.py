#!/usr/bin/env python3
"""
FIFO Caching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching Class with Base Caching as Base class
    """

    def __init__(self):
        """
        Constructor method
        """
        super().__init__()

    def put(self, key, item):
        """
        Stores Item in cache system
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > super().MAX_ITEMS:
                firstKey = list(self.cache_data)[0]
                del self.cache_data[firstKey]
                print('DISCARD: {}'.format(firstKey))

    def get(self, key):
        """
        Returns Value of key specified
        """
        key_value = self.cache_data.get(key)

        if not key_value or not key:
            return None

        return key_value
