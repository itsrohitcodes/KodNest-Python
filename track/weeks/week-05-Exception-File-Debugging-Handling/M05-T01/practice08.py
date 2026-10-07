# Handle Job Requirement Processing Errors

# Write your code here
try:
    student_exp = int(input())
    require_exp = int(input())

    exp_ratio = student_exp / require_exp

    print("Experience Ratio:", exp_ratio)

except ValueError:
    print("Invalid experience")

except ZeroDivisionError:
    print("Required experience cannot be zero")