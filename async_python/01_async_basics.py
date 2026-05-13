# Async Python (async / await):
# Async Python allows programs to:
# handle waiting efficiently

# Used heavily in:
# FastAPI
# APIs
# AI systems
# chat apps
# databases
# web scraping

# import time
# def task(name):
#     print(f"{name} started")
#     time.sleep(2)                             #hold 2 sec then print
#     print(f"{name} finished")
# task("task1")
# task("task2")

# async

# Creates coroutine function.

# async def hello():

# This function behaves differently from normal function.

# await

# Pauses current coroutine:

# without blocking entire program
# await asyncio.sleep(2)

import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")
# 
async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())