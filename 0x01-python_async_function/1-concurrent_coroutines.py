#!/usr/bin/env python3
'''1. Let's execute multiple coroutines at the same time with async
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawn wait_random n times with the specified max_delay
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delay = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
