# Add and Display Student Profiles

# Class for student profile
class StudentProfile:
    # Initialize the object
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    # String representation of the object
    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"

# Class for placement manager
class PlacementManager:
    # Initialize the object
    def __init__(self):
        self.student_profiles = []

    # Method to add a student profile
    def add_student_profile(self, student_profile):
        # Add the received student object
        self.student_profiles.append(student_profile)

    # Method to display student profiles
    def display_student_profiles(self):
        # Handle an empty collection
        if not self.student_profiles:
            print("No student profiles available")
            return

        # Display all student profiles
        print("STUDENT PROFILES")
        for student in self.student_profiles:
            print(student)

# Create a PlacementManager object
manager = PlacementManager()

# Get the number of students
n = int(input())

# Loop n times to get student details
for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    # Create a new object
    student = StudentProfile(student_id, name, course)
    
    # Add the object to the manager
    manager.add_student_profile(student)

# Display all student profiles
manager.display_student_profiles()
