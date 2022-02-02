#!/usr/bin/env python3
"""
    randomly waiting
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """somethings going to happen bets on Traceback??"""
    returnList = []

    
    returnList = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    result = []
    for task in asyncio.as_completed(returnList):
        result.append(await task)

    return result
