#!/usr/bin/env python3
import random
import asyncio
import time

async def sleep_random():
    value = random.uniform(0, 3)
    print(value)

    await asyncio.sleep(2)
    p = value + 1
    print(p)

async def main():
    await asyncio.gather(sleep_random(), sleep_random())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
