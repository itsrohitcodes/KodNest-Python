# Student eligibility checker
# A student is eligible for a certificate if he scores 60 or above in average, has at least 75% attendance, and has submitted the project.
# Read marks, attendance and project completion status
marks = int(input())
attendance = int(input())
project_completion_status = input()

# Check the academic requirements
if marks >= 60 and attendance >= 75:
    # Check the project completion status
    if project_completion_status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")