# when do coroutins start running?
import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in second)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # start coroutine twice (hopefully they start)
    first_awaitable = print_after("world!", 2)
    second_awaitable = print_after("Hello", 1)
    # wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())

# Wed Aug  9 13:41:30 2023 - world!
# Wed Aug  9 13:41:31 2023 - Hello
