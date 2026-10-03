# Sort Employee Records According to Salary

n = int(input())
employees = []

for _ in range(n):
    name, salary = input().split()
    employees.append((name, int(salary)))

# Write your code here
sorted_employees = sorted(employees, key = lambda i : i[1])

for name, salary in sorted_employees:
    print(name, salary)