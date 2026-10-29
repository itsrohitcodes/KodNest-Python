# Generate Numbers Using yield

def generate_numbers (n):
    # Write your code here
    for i in range(1, n+1):
        yield i

n = int(input())
numbers = list(generate_numbers(n))

if numbers:
    print(*numbers)
else:
    print("No numbers")