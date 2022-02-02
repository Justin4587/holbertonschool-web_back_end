#!/usr/bin/env python3
"""
    randomly waiting
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """somethings going to happen bets on Traceback??"""
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
