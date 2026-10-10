# Validate Positive Seats

seats = int(input())

# Write your code here
try:
    if seats < 0:
        raise ValueError

    print("Seats available")

except ValueError:
    print("Invalid seat count")