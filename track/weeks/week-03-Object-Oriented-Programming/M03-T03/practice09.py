# Create MatchScoreCalculator as a child class

class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MatchScoreCalculator(SkillAnalyzer):
    # Add calculate_match_score()
    def calculate_match_score(self):
        matched_skills = self.get_matched_skills()
        if self.required_skills:
            match_percentage = (len(matched_skills) / len(self.required_skills)) * 100
        else:
            match_percentage = 0

        return match_percentage


student_skills = input().split()
required_skills = input().split()

# Create the calculator and display the score
skills = MatchScoreCalculator(student_skills, required_skills)
score = skills.calculate_match_score()

print(f"Match Score: {score:.2f}%")