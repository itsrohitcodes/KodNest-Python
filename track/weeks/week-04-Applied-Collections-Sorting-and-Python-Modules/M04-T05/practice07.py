# Use Result Functions in a Student Program

# pyrefly: ignore [missing-import]
from result_utils import calculate_total, get_grade

student_name = "Neha"
marks = [85, 90, 95]

total = calculate_total(marks)
average = total / len(marks)
grade = get_grade(average)

print("Student:", student_name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)