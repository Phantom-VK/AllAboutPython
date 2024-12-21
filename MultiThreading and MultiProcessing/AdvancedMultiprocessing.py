from concurrent.futures import ProcessPoolExecutor
import os

def task(name):
    print(f"Process {name} running on PID: {os.getpid()}")

with ProcessPoolExecutor(max_workers=3) as executor:
    executor.map(task, [0, 1, 2])

# Output:
# Process 0 running on PID: 12345
# Process 1 running on PID: 12346
# Process 2 running on PID: 12347
