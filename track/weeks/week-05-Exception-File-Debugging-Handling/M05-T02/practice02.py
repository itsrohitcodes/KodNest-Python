# Validate Positive Salary

salary = int(input())

# Write your code here
try:
    if salary <= 0:
        raise ValueError

    print("Valid salary")

except ValueError:
    print("Invalid salary")