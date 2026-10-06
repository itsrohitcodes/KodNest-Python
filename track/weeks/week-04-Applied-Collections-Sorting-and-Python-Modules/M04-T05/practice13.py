# Structure a Student Management Program

# pyrefly: ignore [missing-import]
from student_utils import calculate_average
# pyrefly: ignore [missing-import]
from result_utils import get_result
# pyrefly: ignore [missing-import]
from search_utils import search_student

students = ["Asha", "Ravi", "Neha", "Imran"]
student_name = "Ravi"
marks = [65, 75, 85]

found = search_student(students, student_name)
average = calculate_average(marks)
result = get_result(average)

print("Student:", student_name)
print("Found:", found)
print("Average:", average)
print("Result:", result)