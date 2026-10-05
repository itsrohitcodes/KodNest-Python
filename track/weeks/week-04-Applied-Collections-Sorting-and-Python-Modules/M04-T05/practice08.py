# Combine Multiple Reusable Operations

# pyrefly: ignore [missing-import]
from student_utils import calculate_average
# pyrefly: ignore [missing-import]
from result_utils import get_result, get_grade

student_name = "Imran"
marks = [68, 74, 80]

average = calculate_average(marks)
result = get_result(average)
grade = get_grade(average)

print("Student:", student_name)
print("Average:", average)
print("Result:", result)
print("Grade:", grade)