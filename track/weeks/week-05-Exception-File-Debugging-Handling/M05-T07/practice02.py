# Generate Even Numbers Using a Generator

def generate_even_numbers(limit):
    # Write your code here
    for i in range(1, limit+1):
        if i % 2 == 0:
            yield i

limit = int(input())
numbers = list(generate_even_numbers(limit))

if numbers:
    print(*numbers)
else:
    print("No even numbers")