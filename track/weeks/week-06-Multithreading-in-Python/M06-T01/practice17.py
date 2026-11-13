# Control Concurrent Student Data Loading Using Semaphore

import threading
import time

student_data = {
    "S101": ("Ananya", 88, 81),
    "S102": ("Rahul", 72, 90),
    "S103": ("Meera", 90, 55),
    "S104": ("Kabir", 75, 60),
    "S105": ("Sara", 60, 45),
    "S106": ("Rohan", 93, 88)
}

n = int(input())
student_ids = [input().strip() for _ in range(n)]

semaphore = threading.Semaphore(2)
results = [None] * n

def load_student(index, student_id):
    # Access the student_data service inside with semaphore:
    with semaphore:
        # Simulate loading using time.sleep(0.02).
        time.sleep(0.02)

        name, attendance, score = student_data[student_id]

        # Determine the student's status.
        if attendance >= 75 and score >= 60:
            status = "Ready"
            is_ready = True
        else:
            status = "Needs Support"
            is_ready = False

        # Store (message, is_ready) in results[index].
        message = (
            f"{student_id} | {name} | Attendance: {attendance}% "
            f"| Score: {score} | Status: {status}"
        )

        results[index] = (message, is_ready)


threads = []

# Start one thread for every requested student ID.
for index, student_id in enumerate(student_ids):
    t = threading.Thread(
        target=load_student,
        args=(index, student_id)
    )

    threads.append(t)

for t in threads:
    t.start()

# Wait until all student records have been loaded.
for t in threads:
    t.join()

# Print each stored message in input order.
for message, is_ready in results:
    print(message)

# Print the number of Ready students.
ready_count = sum(is_ready for message, is_ready in results)

print("Ready Students:", ready_count)