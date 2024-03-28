import asyncio
#1
#The “async def” expression defines a coroutine.
#Coroutines are concurrent tasks in asyncio programs. Coroutines are unlike thread-based and process-based concurrency commonly used in Python.
#Multithreading uses threads in a single process,
# multiprocessing spawns separate processes
#while asyncio leverages an event loop and coroutines for cooperative multitasking.
async def main():
    print("First")
    #The await keyword is used to pause the execution of the coroutine until the called coroutine completes.
    await foo('Second')
    print('Last')

async def foo(text):
    print(text)
    #We call asyncio. sleep() when we want to block or suspend the current coroutine for some time.
    await asyncio.sleep(1)

#asyncio. run(main()): This is the main entry point to execute the async program. It runs the main() coroutine and ends when the main() coroutine completes.
asyncio.run(main())

#2
async def main():
    print("First")
    #It submits the coroutine to run "in the background", i.e. concurrently with the current task and all other tasks,
    # switching between them at await points. It returns an awaitable handle called a "task" which you can also use to cancel the execution of the coroutine.
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
    value = await task1
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
    #We can use asyncio. gather to run multiple coroutines concurrently and wait for all of them to complete.
    # The advantage of using asyncio.gather is that it allows you to run multiple coroutines concurrently without blocking the event loop.
    await asyncio.gather(task1(), task2(), task3())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nAll tasks completed in {:.2f} seconds".format(elapsed_time))
# Run the event loop
asyncio.run(main())


