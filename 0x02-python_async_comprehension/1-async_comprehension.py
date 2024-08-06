#!/usr/bin/env python3
"""
This module contains coroutine definition, async_comprehension that
returns 10 random numbers
"""


import asyncio
from typing import Generator


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Returns list of random numbers using async generator
    """
    return [i async for i in async_generator()]
