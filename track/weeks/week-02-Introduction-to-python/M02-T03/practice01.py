# Read and display list number

# Number of integers to read
n = int(input())
numbers = []

# Read n integers and add them to the list
for i in range(n):
    number = int(input())
    numbers.append(number)

# Display list
print(numbers)