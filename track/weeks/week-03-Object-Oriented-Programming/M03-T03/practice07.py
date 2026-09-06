# Extend a Parent Profile Summary Method

class Profile:
    def __init__(self, name):
        self.name = name

    def summary(self):
        return f"Name: {self.name}"


class StudentProfile(Profile):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    # Override summary() here
    def summary(self):
        parent_summary = super().summary()
        return f"{parent_summary}\nCourse: {self.course}"


name = input().strip()
course = input().strip()

# Create the object and print its summary
student = StudentProfile(name, course)

print(student.summary())
