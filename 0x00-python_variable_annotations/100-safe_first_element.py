#!/usr/bin/env python3
"""
    Take a wild Guess a, pi, i
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """somethings going to happen bets on Traceback?? """
    if lst:
        return lst[0]
    else:
        return None
