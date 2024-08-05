#!/usr/bin/env python3
"""
This module contains function definition for the fol. asynchronous coroutine
    wait_random - Returns a random delay between zero an d max_delay
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """
    Waits for a random delay then returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
