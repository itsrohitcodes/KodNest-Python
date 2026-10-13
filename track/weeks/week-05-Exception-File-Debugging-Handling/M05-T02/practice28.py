# Validate an Online Purchase

class InvalidQuantityError(Exception):
    pass

class PurchaseLimitError(Exception):
    pass

quantity = int(input())
amount = int(input())

# Write your code here
try:
    if quantity < 1 or quantity > 5:
        raise InvalidQuantityError("Quantity must be between 1 and 5")

    if amount > 10000:
        raise PurchaseLimitError("Purchase amount cannot exceed 10000")

    print("Purchase successful")

except InvalidQuantityError as e:
    print(e)

except PurchaseLimitError as e:
    print(e)