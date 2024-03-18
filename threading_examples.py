import threading
import time

#1
done = False

def printer():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

printer()
input("Press Enter To Quit")
done = True

#2 multithreading
done = False

def printer():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)
first = threading.Thread(target=printer)
first.start()

input("Press Enter To Quit")
done = True

#3 if nothing else is running quit this thread
done = False

def printer():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)
first = threading.Thread(target=printer, daemon=True)
first.start()

input("Press Enter To Quit")
done = True

#4 pass args (TUPLE)

done = False

def printer(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"\n{text}: {counter}")
first = threading.Thread(target=printer, daemon=True, args=("ABC",))
first.start()
second = threading.Thread(target=printer, daemon=True, args=("XYZ",))
second.start()

input("Press Enter To Quit")
done = True


#5 join method

done = False

def printer(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"\n{text}: {counter}")
first = threading.Thread(target=printer, daemon=True, args=("ABC",))
first.start()
second = threading.Thread(target=printer, daemon=True, args=("XYZ",))
second.start()

first.join()
second.join()
#not to continue until both threads finish
input("Press Enter To Quit")
done = True

#6 loop

done = False

def printer(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"\n{text}: {counter}")

threads = []

for i in range(11):
    t = threading.Thread(target=printer, args=(f"Thread {i}",))
    t.start()

for thread in threads:
    thread.join()

#not to continue until both threads finish
input("Press Enter To Quit")
done = True

#7 thread pool executor
import concurrent.futures


done = False

def printer(text):
    time.sleep(1)
    #!!!
    return f"Finished {text}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    t1 = executor.submit(printer, "ABC")
    t2 = executor.submit(printer, "XYZ")
    print(t1.result())
    print(t2.result())

threads = []




#8 thread pool executor with loop
import concurrent.futures


done = False

def printer(text):
    time.sleep(1)
    #!!!
    return f"Finished {text}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(printer, f"ABC {i}") for i in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

threads = []


#8 different seconds (order)
import concurrent.futures

done = False

def printer(text, sec):
    time.sleep(sec)
    #!!!
    return f"Finished {text}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(printer, text=f"ABC {i}", sec=i) for i in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

threads = []


#8 using map function
import concurrent.futures

done = False

def printer(sec):
    print(f"\nSleeping for {sec} seconds")
    time.sleep(sec)
    #!!!
    return f"\nFinished Sleeping for {sec} seconds"

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    results = executor.map(printer, seconds)

    #exceptions will be raiced here not while threading
    for result in results:
        print(result)




#8 exception / not yet
import concurrent.futures

done = False

def printer(sec):
    print(f"\nSleeping for {sec} seconds")
    time.sleep(sec)
    #!!!
    return f"\nFinished Sleeping for {sec} seconds"

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    results = executor.map(printer, seconds)

    #exceptions will be raiced here not while threading
    for result in results:
        print(result)




