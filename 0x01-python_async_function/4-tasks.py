#!/usr/bin/env python3
"""
    randomly waiting
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """somethings going to happen bets on Traceback??"""
    retList = []

    retList = [asyncio.create_task(task_wait_random(max_delay)) for i in range(n)]
    result = []
    for task in asyncio.as_completed(retList):
        result.append(await task)

    return result
