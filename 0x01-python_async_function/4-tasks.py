#!/usr/bin/env python3
"""
This module contains the following function:
    task_wait_n - Returns a list of delays
"""


import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs task_wait_random n number of times and returns a list of delays
    """
    dlys = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n))
    )
    return sorted(dlys)
