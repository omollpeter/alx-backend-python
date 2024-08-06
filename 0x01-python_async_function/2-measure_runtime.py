#!/usr/bin/env python3
"""
This module contains the following coroutine
    measure_time - Returns the toatl execution time for a corotine
"""


import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the toatl execution time for a corotine
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() / s
    return total / n
