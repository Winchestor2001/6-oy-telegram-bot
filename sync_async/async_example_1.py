import asyncio
import time


async def sleep1():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)


async def sum1(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep1()
        total += number
    print(f'Task {name}: Sum = {total}\n')


start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum1("A", [1, 2])),
    loop.create_task(sum1("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end - start:.2f} sec')
