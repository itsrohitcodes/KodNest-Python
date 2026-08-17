# Extend the Manager Class with a search or filter feature

# Create the StudentProfile class
class StudentProfile:
    # Initialize the object
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    # String representation of the object
    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"

# Create the PlacementManager class
class PlacementManager:
    # Initialize the object
    def __init__(self):
        self.student_profile = []

    # Add a student profile
    def add_student_profile(self, student): 
        self.student_profile.append (student)

    # Find the students based on the course
    def filter_students_by_course(self, search_course):
        # List to store the matching students
        matching_course = []

        # Loop through the student profiles
        for student in self.student_profile:
            if student.course.lower() == search_course.lower():
                matching_course.append(student)
        return matching_course

# Take the student details
manager = PlacementManager()

# Number of students
n = int(input())

# Loop n times to get the details
for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    # Create a new object 
    student = StudentProfile(student_id, name, course)

    # Add the object 
    manager.add_student_profile(student)

# Take the course to be searched
search_course = input().strip()

# Find the students based on the course
result = manager.filter_students_by_course(search_course)

# Filter and display the matching students
if result:
    for student in result: 
        print(student)
else:
    print(f"No students found for course: {search_course}")