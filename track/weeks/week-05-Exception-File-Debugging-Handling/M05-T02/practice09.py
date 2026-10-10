# Validate Withdrawal Amount

amount = int(input())

# Write your code here
try:
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than 0")

    print("Valid withdrawal amount")

except ValueError as e:
    print(e)