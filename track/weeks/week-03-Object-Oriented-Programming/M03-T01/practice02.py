# Create two StudentProfiles with Independent Data

class StudentProfile:
    def __init__(self, student_id, name, course):
        # Store the received values in instance variables
        self.student_id = student_id
        self.name = name
        self.course = course

# Get input values
first_id = int(input())
first_name = input().strip()
first_course = input().strip()

second_id = int(input())
second_name = input().strip()
second_course = input().strip()

# Create the first StudentProfile object
first_student = StudentProfile(first_id, first_name, first_course)

# Create the second StudentProfile object
second_student = StudentProfile(second_id, second_name, second_course)

# Print the first student's data
print(f"Student 1")
print(f"ID: {first_student.student_id}")
print(f"Name: {first_student.name}")
print(f"Course: {first_student.course}")

# Print the second student's data
print(f"Student 2")
print(f"ID: {second_student.student_id}")
print(f"Name: {second_student.name}")
print(f"Course: {second_student.course}")