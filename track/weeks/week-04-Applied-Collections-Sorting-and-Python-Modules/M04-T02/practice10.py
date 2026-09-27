# Build a Number to Square Dictionary

def build_square_dictionary(numbers):
    # Write your dictionary comprehension here
    res = {i:i**2 for i in numbers}

    return res


n = int(input())
numbers = list(map(int, input().split()))

square_by_number = build_square_dictionary(numbers)

for number, square in square_by_number.items():
    print(number, square)