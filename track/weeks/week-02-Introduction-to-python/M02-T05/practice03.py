# Create a Student Profile from user input

# Define StudentProfile class
class StudentProfile:
    # Initialize the object
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        is_placed
    ):
        # Store all received values as instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
    # Return the complete profile in the required format
        placement = ("Placed" if self.is_placed else "Not Placed")

        return (
            f"STUDENT PROFILE \n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score}\n"
            f"Placement Status: {placement}\n"
        )

# Get the user inputs
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
placement_input = input().strip()

# Convert placement_input into a Boolean value
if placement_input == "YES" or placement_input == "yes" or placement_input == "Yes":
    placement_input = True
else:
    placement_input = False

# Create a StudentProfile object using keyword arguments
student = StudentProfile(student_id, name, course, score, placement_input)

# Print the student profile
print(student)