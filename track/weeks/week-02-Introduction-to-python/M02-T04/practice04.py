# Display student details using different arguments types

# defining the function to display the student details
def display_student(name, course, level):
    print(f"{name} | {course} | {level}")

# calling the function with different arguments
display_student("Aarav", "Python", "Beginner") 
display_student(name="Meera", course="Java", level="Intermediate") 
display_student("Kabir", course="SQL", level="Beginner")