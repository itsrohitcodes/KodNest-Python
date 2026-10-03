# Calculate the Total Salary of Every Department

n = int(input())
departments = {}

for _ in range(n):
    data = input().split()
    department = data[0]
    salaries = list(map(int, data[1:]))

    departments[department] = salaries

# Write your code here
for department, salaries in departments.items():
    total_salary = sum(salaries)
    print(f"{department}: {total_salary}")
