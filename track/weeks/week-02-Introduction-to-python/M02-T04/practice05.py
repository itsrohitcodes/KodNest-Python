# Observe a shared default list

# Define the function to add the student
def add_student(name, students=[]):
    # Write your code here
    students.append(name)
    print(students)

# reading the inputs
first_name = input()
second_name = input()
third_name = input()

# calling the function
add_student(first_name)
add_student(second_name)
add_student(third_name)