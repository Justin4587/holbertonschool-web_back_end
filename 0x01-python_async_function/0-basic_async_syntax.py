#!/usr/bin/env python3
"""
    randomly waiting
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """somethings going to happen bets on Traceback?? (comment still applies) """
    waitTime = max_delay * random.uniform(0, max_delay)
    await asyncio.sleep(waitTime)
    return waitTime
