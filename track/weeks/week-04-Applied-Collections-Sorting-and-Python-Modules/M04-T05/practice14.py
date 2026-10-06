# Extend the Student Management System

# pyrefly: ignore [missing-import]
from student_utils import calculate_average
# pyrefly: ignore [missing-import]
from result_utils import get_result, get_grade
# pyrefly: ignore [missing-import]
from search_utils import search_student

students = ["Asha", "Ravi", "Neha", "Imran"]
student_name = "Neha"
marks = [88, 92, 90]

found = search_student(students, student_name)
average = calculate_average(marks)
result = get_result(average)
grade = get_grade(average)

print("Student:", student_name)
print("Found:", found)
print("Average:", average)
print("Result:", result)
print("Grade:", grade)