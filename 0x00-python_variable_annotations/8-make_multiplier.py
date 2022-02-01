#!/usr/bin/env python3
"""
 Take a wild Guess a, pi, i
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
  """somethings going to happen bets on Traceback?? """
  return lambda x: x * multiplier
