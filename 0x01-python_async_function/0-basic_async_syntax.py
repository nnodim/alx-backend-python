#!/usr/bin/env python3
'''Task 0. The basics of async
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    # generate a random float
    delay = random.random() * max_delay
    # wait for the delay using asyncio.sleep
    await asyncio.sleep(delay)
    # return the delay
    return delay
