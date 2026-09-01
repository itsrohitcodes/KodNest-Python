# Update a Student's Experience and Skills

class StudentProfile:
    def __init__(self, name, experience, skills):
        # Store the initial student data
        self.name = name
        self.experience = experience
        self.skills = skills

    def update_experience(self, new_experience): 
        # Replace the current experience
        self.experience = new_experience

    def add_skill(self, new_skill):
        # Add the new skill to the existing list
        self.skills.append(new_skill)

#Getting input from the user
name = input().strip()
experience = int(input())
skills = input().split()
new_experience = int(input())
new_skill = input().strip()


# Create one StudentProfile object
student = StudentProfile(name, experience, skills)

# Update the student's experience
StudentProfile.update_experience(student, new_experience)

# Add the new skill
StudentProfile.add_skill(student, new_skill)

# Print the updated profile
print(f"Name: {student.name}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")