# Handle an Invalid Bank Transaction

class InvalidTransactionError(Exception):
    pass

balance = int(input())
amount = int(input())

# Write your code here
try:
    if amount > balance:
        raise InvalidTransactionError("Transaction amount exceeds balance")
        
    print("Transaction successful")
    
except InvalidTransactionError as e:
    print(e)