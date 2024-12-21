import threading
import time


def task(name):
    print(f"Thread {name} starting")
    time.sleep(2)  # Simulate a time-consuming task (e.g., I/O)
    print(f"Thread {name} finished")


# Create and start multiple threads
threads = [threading.Thread(target=task, args=(i,)) for i in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()

# Output:
# Thread 0 starting
# Thread 1 starting
# Thread 2 starting
# (After ~2 seconds)
# Thread 0 finished
# Thread 1 finished
# Thread 2 finished
