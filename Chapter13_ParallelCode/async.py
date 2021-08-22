import sys
import asyncio


async def foo():
    print('start')
    await asyncio.sleep(2.0)
    print('end')


async def main_await() -> int:
    print('before await')
    await foo()
    print('after await')
    return 0


async def main_task() -> int:
    print('before await')
    task = asyncio.create_task(foo())
    print('after await')
    await task
    return 0


if __name__ == "__main__":
    # code = asyncio.run(main_await())
    code = asyncio.run(main_task())
    sys.exit(code)
