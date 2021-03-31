import threading

def hello(num):
    print(f'Hello from Thread {num}')

threads = []

for c in range(50):
    t = threading.Thread(target=hello, args = [50-c])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()