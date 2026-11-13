# Protect Shared Student Match Results Using Lock

import threading
import time

required_skills = [skill.strip() for skill in input().split(",")]
n = int(input())
students = []

for _ in range(n):
    name = input().strip()
    skills = [skill.strip() for skill in input().split(",")]
    students.append((name, skills))


shared = {"results": {}, "eligible": 0}
lock = threading.Lock()


def match_student(name, skills):
    time.sleep(0.01)

    # Count the job-required skills present in the student's skills.
    match_count = 0

    for skill in required_skills:
        if skill in skills:
            match_count += 1

    # Determine whether the student is Eligible.
    if match_count >= 2:
        status = "Eligible"
    else:
        status = "Not Eligible"

    # Use with lock: to store the match result and update
    with lock:
        shared["results"][name] = (match_count, status)

        if status == "Eligible":
            # the shared eligible-student counter.
            shared["eligible"] += 1


threads = []

# Create and start one thread for each student.
for name, skills in students:
    worker = threading.Thread(
        target=match_student,
        args=(name, skills)
    )

    threads.append(worker)
    worker.start()


# Wait for every thread to finish.
for worker in threads:
    worker.join()


# Print results in the original student order.
for name, skills in students:
    match_count, status = shared["results"][name]
    print(f"{name} | Matched Skills: {match_count} | Status: {status}")


# Finally, print the eligible-student count.
print(f"Eligible Students: {shared['eligible']}")