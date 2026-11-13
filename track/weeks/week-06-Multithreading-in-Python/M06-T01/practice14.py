# Safely Update a Shared Job Processing Counter

import threading
import time

n = int(input())
vacancies_list = [int(input()) for _ in range(n)]

stats = {"processed": 0, "open": 0, "positions": 0}
lock = threading.Lock()

def process_job(vacancies):
    time.sleep(0.01)  # Simulate processing a posting

    # Use with lock: to update the shared counters safely.
    with lock:
        stats["processed"] += 1

        if vacancies > 0:
            stats["open"] += 1

        stats["positions"] += vacancies


threads = []

# Create and start one thread for each vacancy count.
for vacancies in vacancies_list:
    t = threading.Thread(
        target=process_job,
        args=(vacancies,)
    )

    threads.append(t)

for t in threads:
    t.start()

# Wait for all threads to finish.
for t in threads:
    t.join()

# Print the three final counters.
print("Jobs processed:", stats["processed"])
print("Open job postings:", stats["open"])
print("Available positions:", stats["positions"])