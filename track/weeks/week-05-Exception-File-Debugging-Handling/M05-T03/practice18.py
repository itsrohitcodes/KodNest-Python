# Load Structured Data from a JSON File

import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student["name"])
print(student["score"])