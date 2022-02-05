#!/usr/bin/env python3
"""
    randomly waiting
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """somethings going to happen bets on Traceback??"""
    return asyncio.create_task(wait_random(max_delay))
