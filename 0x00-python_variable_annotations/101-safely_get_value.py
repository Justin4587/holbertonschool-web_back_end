#!/usr/bin/env python3
"""
    Take a wild Guess a, pi, i
"""

from typing import Mapping, Any, TypeVar, Union
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]
                     ) -> Union[Any, None]:
    """somethings going to happen bets on Traceback?? """
    if key in dct:
        return dct[key]
    else:
        return default
