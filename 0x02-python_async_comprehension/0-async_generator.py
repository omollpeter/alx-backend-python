#!/usr/bin/env python3
"""
This module contains coroutine definition, async_generator
"""


import asyncio
import random
from typing import Generator, Any


async def async_generator() -> Generator[float, None, None]:
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
