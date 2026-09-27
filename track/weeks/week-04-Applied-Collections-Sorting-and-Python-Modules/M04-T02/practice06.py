# Extract Positive Numbers from a List

def extract_positive_numbers(numbers):
    # Write your list comprehension here
    positive = [i for i in numbers if i > 0]

    return positive


n = int(input())
numbers = list(map(int, input().split()))

positive_numbers = extract_positive_numbers(numbers)

if positive_numbers:
    print(*positive_numbers)
else:
    print("No positive numbers")