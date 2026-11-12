# Collect Results from Concurrent Processing Tasks

from concurrent.futures import ThreadPoolExecutor
import time

n = int(input())
students = []

for _ in range(n):
    name = input().strip()
    completed = int(input())
    students.append((name, completed))


def check_progress(record):
    time.sleep(0.05)
    # Return a tuple containing the student's name and status
    name, completed = record

    if completed >= 8:
        status = "On Track"
    else:
        status = "Needs Practice"

    return name, status


# Create a ThreadPoolExecutor with 3 workers.
with ThreadPoolExecutor(max_workers=3) as executor:

    # Process students using executor.map() and collect the results.
    results = list(executor.map(check_progress, students))


# Print each student's status in input order.
on_track_count = 0

for name, status in results:
    print(f"{name} : {status}")

    if status == "On Track":
        on_track_count += 1


# Count and print the total number of students who are On Track.
print(f"Students On Track: {on_track_count}")