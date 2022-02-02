#!/usr/bin/env python3
"""
    randomly waiting
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """somethings going to happen bets on Traceback??"""
    waited = random.random() * max_delay
    await asyncio.sleep(waited)
    return waited
