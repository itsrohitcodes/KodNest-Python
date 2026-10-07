# Safely Read Student Experience 

# Read the student experience and handle invalid input
student_experience = input()

try:
    student_experience = int(student_experience)
    print("Experience:", student_experience)

except ValueError:
    print("Invalid experience")