# Build a Polymorphic Analyzer runner

from abc import ABC, abstractmethod

class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

    @abstractmethod
    def analyze(self):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        # Return match-score result
        match_skills = self.get_matched_skills()
        score = (len(match_skills) / len(self.required_skills)) * 100
        return f"Match Score: {score:.2f}%"

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        # Return missing-skills result
        missing_skills = self.required_skills - self.student_skills
        missing_skills = sorted(missing_skills)

        if missing_skills:
            return f"Missing Skills: {', '.join(missing_skills)}"

        return f"Missing Skills: None"

def run_analyzers(analyzers):
    # Process every analyzer using one loop
    for analyze in analyzers:
        print(analyze.analyze())

student_skills = input().split()
required_skills = input().split()

# Create analyzer objects, store them in one list and run them
analyzer = [
    MatchScoreCalculator(student_skills, required_skills),
    MissingSkillDetector(student_skills, required_skills)
]

run_analyzers(analyzer)