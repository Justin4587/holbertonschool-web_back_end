#!/usr/bin/env python3
"""
    helper function that returns index for page/s
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ hopefully returns start and end index for pages """

    return ((page * page_size) - page_size, page * page_size)
