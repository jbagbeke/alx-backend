#!/usr/bin/env python3
"""
Caching system that inherits from BasicCache Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching System
    """

    def __init__(self):
        """
        Constructor method for class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns item in a chache system
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns value of key specified from Cache Data
        """
        key_value = self.cache_data.get(key)

        if not key_value or not key:
            return None

        return key_value
