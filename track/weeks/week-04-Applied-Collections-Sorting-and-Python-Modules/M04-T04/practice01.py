# Store Subjects and Marks Inside Student Records

n = int(input())
students = []

for _ in range(n):
    name, python_mark, sql_mark, java_mark = input().split()

    python_mark = int(python_mark)
    sql_mark = int(sql_mark)
    java_mark = int(java_mark)

    students.append({
        "name": name,
        "marks": {
            "Python": python_mark,
            "SQL": sql_mark,
            "Java": java_mark
        }
    })

print(students)