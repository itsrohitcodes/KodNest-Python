# Use the random module

import random

students = ["Asha", "Ravi", "Neha", "Imran"]

selected_student = random.choice(students)
question_number = random.randint(1, 10)

print("Selected Student:", selected_student)
print("Question Number:", question_number)