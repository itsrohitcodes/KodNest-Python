# Fix Errors in Job Processing

job_title = input()
required_experience = int(input())
student_experience = int(input())

if student_experience >= required_experience:
    status = "Eligible"
else:
    status = "Not Eligible"

print("Job: " + job_title)
print("Eligibility: " + status)