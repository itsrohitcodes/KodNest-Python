# Update a Student's Subject Mark

name = input().strip()
python_mark, sql_mark, java_mark = map(int, input().split())

subject = input().strip()
new_mark = int(input())

student = {
    "name": name,
    "marks": {
        "Python": python_mark,
        "SQL": sql_mark,
        "Java": java_mark
    }
}

# Write your code here
student["marks"][subject] = new_mark

print(student)