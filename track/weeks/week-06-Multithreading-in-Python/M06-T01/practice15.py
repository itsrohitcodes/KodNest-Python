# Protect Shared Job Processing Status Using Lock

import threading
import time

n = int(input())
jobs = []

for _ in range(n):
    job_id = input().strip()
    vacancies = int(input())
    verified = int(input())
    jobs.append((job_id, vacancies, verified))

shared = {"statuses": {}, "ready": 0}
lock = threading.Lock()

def process_job(job_id, vacancies, verified):
    time.sleep(0.01)  # Simulate checking the job posting

    # Determine the status using the three rules.
    if vacancies == 0:
        status = "Closed"
    elif verified == 1:
        status = "Ready"
    else:
        status = "Needs Review"

    # Protect the shared status dictionary and Ready counter
    # with the same lock.
    with lock:
        shared["statuses"][job_id] = status

        if status == "Ready":
            shared["ready"] += 1


threads = []

# Create and start one thread for every job.
for job_id, vacancies, verified in jobs:
    t = threading.Thread(
        target=process_job,
        args=(job_id, vacancies, verified)
    )

    threads.append(t)

for t in threads:
    t.start()

# Wait until all threads have finished.
for t in threads:
    t.join()

# Print the saved job statuses in input order.
for job_id, vacancies, verified in jobs:
    print(f"{job_id}: {shared['statuses'][job_id]}")

# Print the total number of Ready jobs.
print("Ready Jobs:", shared["ready"])