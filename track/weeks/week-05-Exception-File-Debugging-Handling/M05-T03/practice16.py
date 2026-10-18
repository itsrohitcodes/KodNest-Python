# Process Structured JSON Data

import json

# Write your code here
data = input()

student = json. loads (data)

scores = student["scores"]
total = sum(scores)

print(student["name"])
print(total)