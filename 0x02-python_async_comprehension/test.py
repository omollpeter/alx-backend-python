#!/usr/bin/env python3

import asyncio

async def aiter(n):
    for i in range(n):
        yield i
        await asyncio.sleep(0.5)

async def test_fun():
    print ([i async for i in aiter(100) if i % 2])

loop = asyncio.get_event_loop()
loop.run_until_complete(test_fun())
