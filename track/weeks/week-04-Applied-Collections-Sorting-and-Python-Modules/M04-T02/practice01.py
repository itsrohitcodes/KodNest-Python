# Create a List of Squares using List Comprehension

def create_squares(numbers):
    # Write your list comprehension here
    square = [i**2 for i in numbers]

    return square


n = int(input())
numbers = list(map(int, input().split()))

squares = create_squares(numbers)
print(*squares)