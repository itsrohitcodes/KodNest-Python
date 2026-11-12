# Process Student Profiles Using Thread Arguments

import threading

name = input().strip()
python_marks = int(input())
sql_marks = int(input())


def process_student_profile(name, python_marks, sql_marks):
    # Check both marks and print the student's status
    if python_marks >= 60 and sql_marks >= 60:
        status = "Ready"
    else:
        status = "Needs Improvement"

    print(f"{name} | Python: {python_marks} | SQL: {sql_marks} | Status: {status}")


# Create a thread and pass all three values using args
thread = threading.Thread(target=process_student_profile, args=(name, python_marks, sql_marks))

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()