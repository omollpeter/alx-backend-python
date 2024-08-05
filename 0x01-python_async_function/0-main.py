#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

# print(asyncio.run(wait_random()))
# print(asyncio.run(wait_random(5)))
# print(asyncio.run(wait_random(15)))

async def toatal():
    for i in range(5):
        r = await asyncio.gather(wait_random())
    return r

print(asyncio.run(toatal()))
