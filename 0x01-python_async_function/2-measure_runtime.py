#!/usr/bin/env python3
"""
    randomly waiting
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """somethings going to happen bets on Traceback??"""
    a = time.time()

    asyncio.run(wait_n(n, max_delay))

    b = time.time()
    
    return (a - b) / n
