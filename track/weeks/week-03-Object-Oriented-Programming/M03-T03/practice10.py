# Create MissingSkillDetector as a child class

class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MissingSkillDetector(SkillAnalyzer):
    # Add get_missing_skills()
    def get_missing_skills(self):
        return self.required_skills - self.student_skills


student_skills = input().split()
required_skills = input().split()

# Create the detector and display missing skills
skills = MissingSkillDetector(student_skills, required_skills)

missing_skill = sorted(skills.get_missing_skills())

if missing_skill:
    print(f"Missing Skills: {', '.join(missing_skill)}")
else:
    print("Missing Skills: None")