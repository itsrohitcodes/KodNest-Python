# Iterate Through Student Names

n = int(input())
students = [input() for _ in range(n)]
k = int(input())

# Write your code here
iter_students = iter(students)

if k == 0:
    print("No students called")
else:
    for _ in range(min(n, k)):
        print(next(iter_students))