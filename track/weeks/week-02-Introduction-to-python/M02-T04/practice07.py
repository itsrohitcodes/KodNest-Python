# Build a Reusable student eligibility Checker

# defining the function to check the eligibility
def check_eligibility(marks, attendance, project_completed):
    # TODO: Check whether all three eligibility conditions are satisfied
    if marks >= 60:
        if attendance >= 75:
            if project_completed == "yes":
                return "Eligible"

    # TODO: Return "Eligible" or "Not Eligible"
    return "Not Eligible"

# Read the student's details
marks = int(input())
attendance = int(input())
project_completed = input().strip().lower()

# Call the function and print the returned result
result = check_eligibility(marks, attendance, project_completed)

# print the result
print(result)