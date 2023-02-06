#!/usr/bin/env python3
import asyncio

wait_random = __import__(0-basic_async_syntax.py).wait_random
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
