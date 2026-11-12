# Wait for Job Processing Tasks to Complete

import threading
import time

job_title = input().strip()
min_experience = int(input())
max_experience = int(input())
min_salary = int(input())
max_salary = int(input())

experience_result = []
salary_result = []

def check_experience(minimum, maximum, result):
    time.sleep(0.1)
    # Append "Valid" or "Invalid" to result
    if minimum < maximum:
        result.append("Valid")
    else:
        result.append("Invalid")


def check_salary(minimum, maximum, result):
    time.sleep(0.1)
    # Append "Valid" or "Invalid" to result
    if minimum < maximum:
        result.append("Valid")
    else:
        result.append("Invalid")


# Create two threads and pass each function its arguments.
thread1 = threading.Thread(
    target=check_experience,
    args=(min_experience, max_experience, experience_result)
)

thread2 = threading.Thread(
    target=check_salary,
    args=(min_salary, max_salary, salary_result)
)

# Start both threads.
thread1.start()
thread2.start()

# Wait for both threads to finish.
thread1.join()
thread2.join()

# Read the results, determine the posting status, and print four lines.
exp_res = experience_result[0]
sal_res = salary_result[0]

if exp_res == "Valid" and sal_res == "Valid":
    status = "Approved"
else:
    status = "Rejected"

print(f"Job: {job_title}")
print(f"Experience Range: {exp_res}")
print(f"Salary Range: {sal_res}")
print(f"Posting Status: {status}")