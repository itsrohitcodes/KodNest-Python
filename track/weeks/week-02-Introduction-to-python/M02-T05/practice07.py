# Search for Student Profile by ID

# Class for student profile
class StudentProfile:
    # Initialize the object
    def __init__(self, student_id, name, course):
        self.student_id = student_id 
        self.name = name
        self.course = course

    # String representation of the object
    def __str_(self):
        return f"{self.student_id} - {self.name} - {self.course}"

# Class for placement manager
class PlacementManager:
    # Initialize the object
    def __init__(self):
        self.student_profiles = []

    # Method to add a student profile
    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    # Method to find a student profile by ID
    def find_student_by_id(self, student_id):
        # Search for and return the matching object
        for student in self.student_profiles:
            if student.student_id == student_id:
                return student
        # Return None if no match is found
        return None

# Create a PlacementManager object
manager = PlacementManager()

# Get the number of student profiles to add
n = int(input())

# Loop n times to get student details
for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    # Create an object
    student = StudentProfile(student_id, name, course)

    # Add the object to the manager
    manager.add_student_profile(student)

# Get the ID to search for
required_id = int(input())

# Find the student
result = manager.find_student_by_id(required_id)

# Display the result
if result is not None: 
    print(result)
else:
    print(f"Student profile with ID {required_id} not found")