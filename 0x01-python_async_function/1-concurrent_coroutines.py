#!/usr/bin/env python3
"""
This module contains the following asynchronous coroutinne:
    wait_n - Returns a list of delays from wait_random coroutine
"""


import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs wait_random n number of times and returns a list of delays
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return delays
