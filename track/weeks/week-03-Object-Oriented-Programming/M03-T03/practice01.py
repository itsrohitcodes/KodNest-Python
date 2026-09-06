# Build a Person and Student Classes

class Person:
    # Create display_name() here
    def display_name(self, name):
        print(f"Student Name: {name}")


class Student(Person):
    pass


name = input().strip()

# Create a Student object and call display_name()
student = Student()

student.display_name(name)