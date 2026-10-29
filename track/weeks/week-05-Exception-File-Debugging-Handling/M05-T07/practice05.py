# Convert a Normal Function into a Generator

def generate_squares (n):
    for number in range(1, n + 1):
        yield number * number

n = int(input())

result = list(generate_squares (n))

if result:
    print(*result)
else:
    print("No squares")