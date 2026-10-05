# Use an Imported Student Class

# pyrefly: ignore [missing-import]
from student_models import Student

student_name = "Ravi"
marks = [72, 80, 88]

student = Student(student_name, marks)
average = student.get_average()
result = student.get_result()

print("Student:", student_name)
print("Average:", average)
print("Result:", result)