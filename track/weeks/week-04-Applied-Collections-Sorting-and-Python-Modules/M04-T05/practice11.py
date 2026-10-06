# Organize Student Record Operations

# pyrefly: ignore [missing-import]
from student_records import create_record, calculate_average

student_name = "Asha"
marks = [82, 76, 88]

record = create_record(student_name, marks)
average = calculate_average(record)

print("Student:", student_name)
print("Average:", average)