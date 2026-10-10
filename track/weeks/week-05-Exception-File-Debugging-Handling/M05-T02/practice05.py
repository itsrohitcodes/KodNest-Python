# Validate Product Stock

stock = int(input())

# Write your code here
try:
    if stock < 0:
        raise ValueError

    print("Valid stock")

except ValueError:
    print("Invalid stock")