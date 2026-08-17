# Create Student Profiles using keyword arguments

# Create StudentProfile class
class StudentProfile:
    # Initialize the object
    def __init__(
        self,
        student_id,
        name,
        course,
        score=0.0,
        is_placed=False
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    # String representation of the object
    def __str__(self):
        placement_status = (
            "Placed" if self.is_placed
            else "Not Placed"
        )

        return(
            f"{self.student_id} |"
            f"{self.name} |"
            f"{self.course} |"
            f"{self.score:.1f} |"
            f"{placement_status}"
        )

# Create student_one using keyword arguments
student_one = StudentProfile(
    # Write your keyword arguments here
    student_id = 101,
    name = "Asha",
    course = "Python",
    score = 85.0,
    is_placed = False
)


# Create student_two using keyword arguments
student_two = StudentProfile(
    # Write your keyword arguments here
    student_id = 102,
    name = "Rahul",
    course = "Java",
)

# Print the student details
print(student_one)
print(student_two)