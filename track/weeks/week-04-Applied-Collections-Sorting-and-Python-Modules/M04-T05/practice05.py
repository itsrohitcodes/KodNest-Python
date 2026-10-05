# Use Imported Functions in a Student Program

# pyrefly: ignore [missing-import]
from student_utils import calculate_average, get_result

student_name = "Asha"
marks = [78, 84, 90]

average = calculate_average(marks)
result = get_result(average)

print("Student:", student_name)
print("Average:", average)
print("Result:", result)