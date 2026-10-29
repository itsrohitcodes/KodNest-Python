# Access List Elements Using an Iterator

n = int(input())
students = [input() for _ in range(n)]

# Write your code here
iter_students = iter(students)

for i in range(n):
    print(next(iter_students))