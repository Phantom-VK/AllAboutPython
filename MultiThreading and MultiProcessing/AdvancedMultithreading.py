from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Thread {name} starting")
    time.sleep(2)  # Simulate I/O
    print(f"Thread {name} finished")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task, [0, 1, 2])

# Output:
# Thread 0 starting
# Thread 1 starting
# Thread 2 starting
# (After ~2 seconds)
# Thread 0 finished
# Thread 1 finished
# Thread 2 finished
