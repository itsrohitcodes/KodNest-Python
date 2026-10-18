# Update Data Stored in a JSON File

import json

with open("student.json", "r") as file:
    student = json.load(file)

student["score"] = 95

with open("student.json", "w") as file:
    json.dump(student, file)