# Validate Product Quantity

quantity = int(input())

# Write your code here
try:
    if quantity <= 0:
        raise ValueError("Quantity must be at least 1")

    print("Valid quantity")

except ValueError as e:
    print(e)    