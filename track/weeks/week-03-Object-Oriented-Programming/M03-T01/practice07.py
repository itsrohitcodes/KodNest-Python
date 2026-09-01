# Protect and Update a Private Student Score

class StudentProfile:
    def __init__(self, name, score):
        self.name = name
        # Store the score in a private attribute
        self.__score = score

    def get_score(self):
        # Return the private score
        return self.__score

    def set_score(self, new_score):
        # Update and return True when the score is valid
        # Return False without updating when it is invalid
        if 0 <= new_score <= 100:
            self.__score = new_score
            return True
        else:
            return False

# Getting input from the user
name = input().strip()
initial_score = int(input())
new_score = int(input())

# Create one StudentProfile object
student = StudentProfile(name, initial_score)

# Call set_score() and store its Boolean result
result = student.set_score(new_score)

# Display the update result
if result is True:
    print("Score Updated")
else:
    print("Invalid Score")

# Display the name and final score
print(f"Name: {student.name}")
print(f"Final Score: {student.get_score()}")