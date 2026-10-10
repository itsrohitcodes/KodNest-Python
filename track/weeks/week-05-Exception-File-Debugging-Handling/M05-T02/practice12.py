# Validate Discount Percentage

discount = int(input())

# Write your code here
try:
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")

    print("Valid discount")

except ValueError as e:
    print(e)