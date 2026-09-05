# Count Created Student Profile Objects

class StudentProfile:
    # Create the class-level object counter
    profile_count = 0

    def __init__(self, name):
        # Store the name
        self.name = name
        # Increase the shared counter
        StudentProfile.profile_count += 1


n = int(input())
students = []

# Read n names and create n StudentProfile objects
for i in range(n):
    name = input().strip()
    profile = StudentProfile(name)
    students.append(name)

# Print the number of created student profiles
print(f"Profiles Created: {StudentProfile.profile_count}")