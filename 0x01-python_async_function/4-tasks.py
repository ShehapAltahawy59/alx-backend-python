#!/usr/bin/env python3
"""
Execute multiple coroutines same time with async
Write async coroutine
takes argument wait_n and max_delay
"""
import asyncio
from typing import List
import random

get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine
    wait_n
    """
    ls = [get(max_delay) for i in range(n)]
    end = [await task for task in asyncio.as_completed(ls)]
    return end
