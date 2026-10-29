# Generate Multiples of a Number

def generate_multiples(number, count):
    # Write your code here
    for i in range(1, count+1):
        yield number * i

number = int(input())
count = int(input())

multiples = list(generate_multiples(number, count))

if multiples:
    print(*multiples)
else:
    print("No multiples")