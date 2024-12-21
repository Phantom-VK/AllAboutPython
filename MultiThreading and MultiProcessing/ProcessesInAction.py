from multiprocessing import Process
import os

def task(name):
    print(f"Process {name} running on PID: {os.getpid()}")

# Create and start multiple processes
processes = [Process(target=task, args=(i,)) for i in range(3)]

for p in processes:
    p.start()

for p in processes:
    p.join()

# Output:
# Process 0 running on PID: 12345
# Process 1 running on PID: 12346
# Process 2 running on PID: 12347
