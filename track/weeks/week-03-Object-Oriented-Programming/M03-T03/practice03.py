# Build a Employee and Developer using Super()

class Employee:
    # Add the constructor
    def __init__(self, name, language):
        self.name = name
        self.language = language


class Developer(Employee):
    # Add the constructor and display_profile()
    def __init__(self, name, language):
        super().__init__(name, language)

    def display_profile(self):
        print(f"Employee: {self.name}")
        print(f"Language: {self.language}")


name = input().strip()
language = input().strip()

# Create a Developer object and display its profile
person = Developer(name, language)

person.display_profile()