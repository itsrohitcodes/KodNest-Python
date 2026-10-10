# Validate Exam Score

score = int(input())

# Write your code here
try:
    if score < 0 or score > 100:
        raise ValueError

    print("Valid score")

except ValueError:
    print("Invalid score")