# Process Different Student Profile Types Uniformly

class StudentProfile:
    def show_profile(self):
        pass


class FresherStudent(StudentProfile):
    def __init__(self, name, graduation_year):
        self.name = name
        self.graduation_year = graduation_year

    def show_profile(self):
        # Write your code here
        return f"{self.name} - Fresher - Graduation Year: {self.graduation_year}"


class ExperiencedStudent(StudentProfile):
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def show_profile(self):
        # Write your code here
        return f"{self.name} - Experienced - Experience: {self.experience} years"


fresher_name = input()
graduation_year = int(input())
experienced_name = input()
experience = int(input())

# Create the two objects
fresher = FresherStudent(fresher_name, graduation_year)
experienced = ExperiencedStudent(experienced_name, experience)

# Store both objects in one list
students = [fresher, experienced]

# Process the list using one loop
for student in students:
    print(student.show_profile())