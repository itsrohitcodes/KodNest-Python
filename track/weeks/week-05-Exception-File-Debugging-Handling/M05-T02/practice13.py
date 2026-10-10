# Create an Exception for Insufficient Balance

class InsufficientBalanceError(Exception):
    pass

balance = int(input())
amount = int(input())

# Write your code here
try:
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    print("Withdrawal allowed")

except InsufficientBalanceError as e:
    print(e)