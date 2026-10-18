# Convert Python Data to JSON Text

import json

# Write your code here
name = input()
score = int(input())

student = {
    "name": name,
    "score": score
}

print(json.dumps(student))