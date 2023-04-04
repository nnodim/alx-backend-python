#!/usr/bin/env python3
'''Task 4. Tasks
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Return the list of all delays (in seconds) for the executed tasks.
    '''
    tasks = [task_wait_random(max_delay) for i in range(n)]
    finished_tasks = []
    for task in asyncio.as_completed(tasks):
        finished_tasks.append(await task)
    return finished_tasks

