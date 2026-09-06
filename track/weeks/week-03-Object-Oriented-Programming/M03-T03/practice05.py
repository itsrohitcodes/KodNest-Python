# Create Fresher and Experience Student Profiles

class StudentProfile:
    # Add the constructor and display_profile()
    def __init__(self, name):
        self.name = name


class FresherStudent(StudentProfile):
    def __init__(self, name):
        super().__init__(name)


class ExperiencedStudent(StudentProfile):
    def __init__(self, name):
        super().__init__(name)


fresher_name = input().strip()
experienced_name = input().strip()

# Create both objects and display their profiles
fresher_student = FresherStudent(fresher_name)
experienced_student = ExperiencedStudent(experienced_name)

print(f"Fresher Student: {fresher_student.name}")
print(f"Experienced Student: {experienced_student.name}")