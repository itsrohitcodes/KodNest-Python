# Group employees according to thier department

def group_employees(employees):
    employees_by_department = {}

    # Write your grouping logic here
    for name, department in employees:
        if department not in employees_by_department:
            employees_by_department[department] = []
        employees_by_department[department].append(name)

    return employees_by_department


n = int(input())
employees = []

for _ in range(n):
    name, department = input().split()
    employees.append((name, department))

employees_by_department = group_employees(employees)

for department, names in employees_by_department.items():
    print(department + ": " + " ".join(names))