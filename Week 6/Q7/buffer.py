import threading
import time
import random

data = 1
dataLimit = input("Enter the data limit for the producer: ")

def producer():
    global data
    global dataLimit
    print("Producer generating data")
    data+=1

def consumer():
    global data
    print("Consumer consuming data")
    data-=1

threads = []

for _ in range(50):
    t = threading.Thread(target=producer)
    t1 = threading.Thread(target=consumer)
    threads.append(t)
    threads.append(t1)

random.shuffle(threads)

for thread in threads:
    thread.start()
    if data == dataLimit:
        print("Data full, producer going to sleep\n")
        time.sleep(0.1)
    if data == 0:
        print("Data null, consumer going to sleep\n")
        time.sleep(0.1)
for thread in threads:
    thread.join()
