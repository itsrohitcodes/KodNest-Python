# Wait for Student Processing Tasks to Complete

import threading
import time

name = input().strip()
attendance = int(input())
marks = int(input())

attendance_result = []
assessment_result = []

def check_attendance(percentage, result):
    time.sleep(0.1)
    # Add "Eligible" or "Not Eligible" to result
    if percentage >= 75:
        result.append("Eligible")
    else:
        result.append("Not Eligible")


def check_assessment(score, result):
    time.sleep(0.1)
    # Add "Passed" or "Failed" to result
    if score >= 60:
        result.append("Passed")
    else:
        result.append("Failed")


# Create one thread for each check.
# Pass the required values using args.
thread1 = threading.Thread(
    target=check_attendance,
    args=(attendance, attendance_result)
)

thread2 = threading.Thread(
    target=check_assessment,
    args=(marks, assessment_result)
)

# Start both threads before waiting.
thread1.start()
thread2.start()

# Wait for both threads to finish.
thread1.join()
thread2.join()

# Read the results and print the four output lines.
print(f"Student: {name}")
print(f"Attendance: {attendance_result[0]}")
print(f"Assessment: {assessment_result[0]}")

if attendance_result[0] == "Eligible" and assessment_result[0] == "Passed":
    print(f"Overall: Ready")
else:
    print(f"Overall: Not Ready")