#!/usr/bin/env python3
""" delay"""

import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, maxdelay: int = 10) -> float:
    """return total_time/n"""

    elapsed_time = float
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, maxdelay))
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time / n
