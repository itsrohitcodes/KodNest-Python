# Product of a List

from functools import reduce

def multiply(x, y):
    # TODO: Implement logic to return the product of x and y
    return x * y

# TODO: Use reduce() to calculate the product of user_numbers
user_numbers = list(map(int, input().split()))
# List of integers for product calculation

total = reduce(multiply, user_numbers)

print(total)