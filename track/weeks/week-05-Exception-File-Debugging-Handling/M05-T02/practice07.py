# Validate Marks with a Clear Error Message

marks = int(input())

# Write your code here
try:
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    print("Valid marks")

except ValueError as e:
    print(e)