#!/usr/bin/env python3
"""
PAGINATION - REST API DESIGN
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index
    and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return tuple([start_index, end_index])


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Using pagination returns required data set list
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        page_index = index_range(page, page_size)

        if page_index[1] > 19419:
            return []

        return self.dataset()[page_index[0]:page_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing the following key-value pairs
        """
        index_rge = index_range(page, page_size)

        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': (page + 1) if index_rge[1] < 19419 else None,
            'prev_page': (page - 1) if page > 1 else None,
            'total_pages': int(19419 / page_size)
        }
