# Build a Simple JSON Based Record Store

import json

with open("students.json", "r") as file:
    students = json.load(file)

new_student = {
    "name": "Kabir",
    "score": 78
}

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file)