import asyncio
#1
async def main():
    print("First")
    await foo('Second')
    print('Last')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

#2
async def main():
    print("First")
    task = asyncio.create_task(foo('Second'))
    print('Last')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

#3
async def main():
    print("First")
    task = asyncio.create_task(foo('Second'))
    await task
    print('Last')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

#4
async def main():
    print("First")
    task = asyncio.create_task(foo('Second'))
    await asyncio.sleep(2)
    print('Last')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

#5
async def main():
    print("First")
    task = asyncio.create_task(foo('Second'))
    await asyncio.sleep(0.5)
    print('Last')

async def foo(text):
    print(text)
    await asyncio.sleep(10)

asyncio.run(main())

# 6
async def fetch_data():
    print("Start Fetching")
    await asyncio.sleep(2)
    print('Done Fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    value = await  task1
    print(value)

asyncio.run(main())

#7 Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the time taken.
import asyncio
import time
async def task1():
    print("Task-1 started")
    await asyncio.sleep(4)
    print("Task-1 completed")
async def task2():
    print("Task-2 started")
    await asyncio.sleep(1)
    print("Task-2 completed")
async def task3():
    print("Task-3 started\n")
    await asyncio.sleep(2)
    print("Task-3 completed")

async def main():
    start_time = time.time()
    await asyncio.gather(task1(), task2(), task3())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nAll tasks completed in {:.2f} seconds".format(elapsed_time))
# Run the event loop
asyncio.run(main())


#8 Write a Python program that uses asyncio queues to simulate a producer-consumer scenario with multiple producers and a single consumer.
import asyncio
import random
async def producer(queue, id):
    for i in range(3):
        item = f"Item: {id}-{i}"
        await queue.put(item)
        print(f"Producer {id} produced-> {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))
async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer consumed {item}")
        queue.task_done()
async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, i)) for i in range(3)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    await queue.put(None)  # Signal the consumer to stop
    await consumer_task
# Run the event loop
asyncio.run(main())