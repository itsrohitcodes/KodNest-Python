# Convert SkillAnalyzer into an Abstract Base Class

from abc import ABC, abstractmethod

class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

    # Add abstract analyze()
    def analyze(self):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        matched = len(self.get_matched_skills())
        required = len(self.required_skills)
        return matched / required * 100

    # Implement analyze()
    def analyze(self):
        match_skills = self.get_matched_skills()
        score = (len(match_skills) / len(self.required_skills)) * 100

        return f"Match Score: {score:.2f}%"

class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        return self.required_skills - self.student_skills

    # Implement analyze()
    def analyze(self):
        missing_skills = self.required_skills - self.student_skills
        missing_skills = sorted(missing_skills)

        if missing_skills:
            return f"Missing Skills: {', '.join(missing_skills)}"
        else:
            return f"Missing Skills: None"

student_skills = input().split()
required_skills = input().split()

# Create both analyzers and print their analyze() results
analyzers = [
    MatchScoreCalculator(student_skills, required_skills),
    MissingSkillDetector(student_skills, required_skills)
]

for analyzer in analyzers:
    print(analyzer.analyze())