#!/usr/bin/env python3
"""
    randomly waiting
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """somethings going to happen bets on Traceback??"""
    a = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    b = time.time()
    
    return (b - a)
