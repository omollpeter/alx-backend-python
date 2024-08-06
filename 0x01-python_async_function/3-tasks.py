#!/usr/bin/env python3
"""
This module contains the following function:
    task_wait_random - Returns asyncio.Task
"""


import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
