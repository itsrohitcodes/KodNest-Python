# Limit Concurrent Student File Processing Tasks

import threading
import time

n = int(input())
limit = int(input())
files = []

for _ in range(n):
    name = input().strip()
    count = int(input())
    files.append((name, count))

semaphore = threading.Semaphore(limit)
results = [None] * n

def process_file(index, name, count):
    # Use with semaphore: to limit concurrent file processing.
    with semaphore:
        # Simulate processing using time.sleep(0.02).
        time.sleep(0.02)

        # Store the formatted result at results[index].
        if count > 0:
            status = "Processed"
        else:
            status = "Empty"

        results[index] = (
            f"{name} | Records: {count} | Status: {status}"
        )

threads = []

# Create and start one thread for each file.
for index, (name, count) in enumerate(files):
    worker = threading.Thread(
        target=process_file,
        args=(index, name, count)
    )

    threads.append(worker)
    worker.start()

# Wait for every thread to finish.
for worker in threads:
    worker.join()

# Print the results in input order.
for result in results:
    print(result)

# Print the number of non-empty files and total records.
files_with_data = sum(1 for name, count in files if count > 0)
total_records = sum(count for name, count in files)

print(f"Files with Data: {files_with_data}")
print(f"Total Records: {total_records}")