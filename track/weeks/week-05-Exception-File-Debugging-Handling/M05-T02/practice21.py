# Handle Invalid Product Quantity

class InvalidQuantityError(Exception):
    pass

quantity = int(input())

# Write your code here
try:

    if quantity <= 0 or quantity > 10:
        raise InvalidQuantityError("Quantity must be between 1 and 10")
    
    print("Quantity accepted")
    
except InvalidQuantityError as e:
    print(e)