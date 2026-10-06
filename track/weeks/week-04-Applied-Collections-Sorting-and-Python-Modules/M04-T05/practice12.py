# Organize Student Search and Result Operations

# pyrefly: ignore [missing-import]
from search_utils import search_student
# pyrefly: ignore [missing-import]
from result_utils import get_result

students = ["Asha", "Ravi", "Neha", "Imran"]
student_name = "Neha"
mark = 78

found = search_student(students, student_name)
result = get_result(mark)

print("Student:", student_name)
print("Found:", found)
print("Result:", result)