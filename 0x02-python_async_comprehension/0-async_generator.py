#!/usr/bin/env python3

from typing import Generator
import random
import asyncio

async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times asynchronously"""
    for i in range(10):
        yield random(0,10)
        await asyncio.sleep(1)
