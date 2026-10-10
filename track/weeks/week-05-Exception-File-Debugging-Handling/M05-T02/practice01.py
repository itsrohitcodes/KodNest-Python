# Validate Minimum Age

age = int(input())

# Write your code here
try:
    if age < 18:
        raise ValueError

    print("Eligible")

except ValueError:
    print("Invalid age")