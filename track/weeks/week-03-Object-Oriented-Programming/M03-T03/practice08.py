# Build the initial SkillAnalyzer class

class SkillAnalyzer:
    # Add the constructor and get_matched_skills()
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


student_skills = input().split()
required_skills = input().split()

# Create the analyzer and display matched skills
skills = SkillAnalyzer(student_skills, required_skills)
matched = sorted(skills.get_matched_skills())

if matched:
    print(f"Matched Skills: {', '.join(matched)}")
else:
    print("Matched Skills: None")