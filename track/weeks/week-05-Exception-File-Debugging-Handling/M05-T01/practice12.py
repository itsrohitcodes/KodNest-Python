# Complete Job Requirement Processing Safely

# Write your code here
try:
    student_exp = int(input())
    required_exp = int(input())

    match_exp = (student_exp / required_exp) * 100

except ValueError:
    print("Invalid experience value")

except ZeroDivisionError:
    print("Required experience cannot be zero")

else:
    print("Experience Match:", match_exp)

finally:
    print("Job requirement processing complete")