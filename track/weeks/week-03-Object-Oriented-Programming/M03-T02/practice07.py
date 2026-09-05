# Normalize Student Skill Names Using a Static Method

class StudentProfile:
    # Create the normalize_skill() static method
    @staticmethod
    def normalize_skill(skill_name):
        word = skill_name.lower().strip().split()
        return "_".join(word)


skill_name = input()

# Normalize the skill using the class name
normalize_skill = StudentProfile.normalize_skill(skill_name)

# Print the normalized skill
print(f"Normalized Skill: {normalize_skill}")