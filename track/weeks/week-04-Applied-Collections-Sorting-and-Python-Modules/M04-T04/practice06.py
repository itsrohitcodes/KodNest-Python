# Calculate the Average Marks of Every Student

n = int(input())
students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(int, data[1:]))

    students.append({
        "name": name,
        "marks": marks
    })

# Write your code here
for student in students:
    name = student["name"]
    marks = student["marks"]

    total = sum(marks)
    average = total / len(marks)

    print(f"{name}: {average:.2f}")
