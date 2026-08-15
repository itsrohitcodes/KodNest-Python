# Create and unpacked a student record

# Read and display student details
name = input()
course = input()
score = int(input())

# Create the tuple
student_record = (name, course, score)

# Unpack the tuple
student_name, student_course, student_score = student_record

# Display the unpacked values
print(f"Name: {student_name}")
print(f"Course: {student_course}")
print(f"Score: {student_score}")