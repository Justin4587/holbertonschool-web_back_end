#!/usr/bin/env python3
"""
    randomly waiting
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """somethings going to happen bets on Traceback??"""
    return [beepsAndBoops async for beepsAndBoops in async_generator()]
