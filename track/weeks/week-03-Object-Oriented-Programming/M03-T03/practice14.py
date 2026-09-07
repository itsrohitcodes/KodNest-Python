# Complete the Skill Analysis System

class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        # Calculate and return the match percentage
        match_skills = self.get_matched_skills()
        score = (len(match_skills) / len(self.required_skills)) * 100
        return score


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        # Return the missing skills
        return self.required_skills - self.student_skills


student_skills = [skill.strip() for skill in input().split(",")]
required_skills = [skill.strip() for skill in input().split(",")]

calculator = MatchScoreCalculator(student_skills, required_skills)
detector = MissingSkillDetector(student_skills, required_skills)

score = calculator.calculate_match_score()
missing = sorted(detector.get_missing_skills())

print(f"Match Score: {score:.1f}%")
print("Missing Skills:", ", ".join(missing) if missing else "None")