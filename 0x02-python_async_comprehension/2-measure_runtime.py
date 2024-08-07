#!/usr/bin/env python3
"""
This module contains the following coroutine
    measure_runtime - Returns the total time for executing four async
                        comprehensions
"""


import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Returns the total time for executing four async comprehensions
    """
    s = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time.perf_counter() - s
