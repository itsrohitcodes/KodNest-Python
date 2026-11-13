# Limit Concurrent Job File Processing Tasks

import threading
import time

n = int(input())
files = []

for _ in range(n):
    name = input().strip()
    total = int(input())
    expired = int(input())
    files.append((name, total, expired))

semaphore = threading.Semaphore(2)
results = [None] * n

def process_file(index, name, total, expired):
    # Use with semaphore: to limit access to the file service.
    with semaphore:
        # Simulate file loading using time.sleep(0.02).
        time.sleep(0.02)

        # Calculate active jobs and determine the file status.
        active = total - expired

        # Store (message, active, is_ready) at results[index].
        if total == 0:
            status = "Empty"
        elif active == 0:
            status = "No Active Jobs"
        else:
            status = "Ready"

        is_ready = (status == "Ready")

        # Store result
        message = f"{name} | Active Jobs: {active} | Status: {status}"
        results[index] = (message, active, is_ready)


threads = []

# Create and start one thread for each file.
for index, (name, total, expired) in enumerate(files):
    t = threading.Thread(
        target=process_file,
        args=(index, name, total, expired)
    )

    threads.append(t)

for t in threads:
    t.start()

# Use join() to wait for every worker.
for t in threads:
    t.join()

# Print file results in their input order.
ready_count = 0
total_active = 0

for message, active, is_ready in results:
    print(message)

    total_active += active

    if is_ready:
        ready_count += 1

# Print the Ready-file count and the total active jobs.
print("Files Ready:", ready_count)
print("Total Active Jobs:", total_active)