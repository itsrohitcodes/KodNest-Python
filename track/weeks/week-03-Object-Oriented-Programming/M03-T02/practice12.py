# Validate and Normalize a student skill using Static methods

class StudentProfile:
    # Create the is_valid_skill() static method
    @staticmethod
    def is_valid_skill(skill_name):
        if skill_name.strip() == "":
            return False

        for ch in skill_name:
            if not (ch.isalpha() or ch == " "):
                return False

        return True

    # Create the normalize_skill() static method
    @staticmethod
    def normalize_skill(skill_name):
        skill_name = skill_name.strip().lower()

        word = skill_name.split()
        skill_name = "_".join(word)

        return skill_name


skill_name = input()

# Validate the skill
if StudentProfile.is_valid_skill(skill_name):
    print("Valid Skill")
    print(f"Normalized Skill: {StudentProfile.normalize_skill(skill_name)}")
else:
    print("Invalid Skill")

# Normalize and print it only when valid