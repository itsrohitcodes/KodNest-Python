# Handle an Invalid Order Amount

class InvalidOrderError(Exception):
    pass

amount = int(input())

# Write your code here
try:
    if amount < 500:
        raise InvalidOrderError("Order amount must be at least 500")
    
    print("Order accepted")
    
except InvalidOrderError as e:
    print(e)