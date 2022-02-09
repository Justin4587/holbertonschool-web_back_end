#!/usr/bin/env python3
"""
    helper function that returns index for page/s
"""
import csv
import math
from typing import List, Tuple, Dict

index_range = __import__('0-simple_helper_function').index_range


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
        """ Its all in the name """

        assert isinstance(page, int) and type(page) is type(page_size)
        assert page > 0 and page_size > 0

        iLikeTheWordTuple = index_range(page, page_size)
        stupid = iLikeTheWordTuple[0]
        loser = iLikeTheWordTuple[1]
        return self.dataset()[stupid:loser]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ the same but HYPER """

        data = self.get_page(page, page_size)
        total = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total - 1 else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total
        }
