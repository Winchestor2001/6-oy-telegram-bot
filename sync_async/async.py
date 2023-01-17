import asyncio


async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    print(s)
    asyncio.run(main())
    e = time.perf_counter() - s
    print(e)
    print(f"End in {e:0.2f} sec")
