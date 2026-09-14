# Test Duplicate and Mixed Case Skill Values

class StudentProfile:
    def __init__(self, skills):
        self.skills = skills


class JobDescription:
    def __init__(self, required_skills):
        self.required_skills = required_skills


class SkillAnalyzer:
    def __init__(self, student, job):
        self.student = student
        self.job = job

    def analyze(self):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        student_skills = []
        required_skills = []

        # Normalize student skills and remove duplicates
        for skill in self.student.skills:
            if skill.strip().lower() != "" and skill.strip().lower() not in student_skills:
                student_skills.append(skill.strip().lower())

        # Normalize required skills and remove duplicates
        for skill in self.job.required_skills:
            if skill.strip().lower() != "" and skill.strip().lower() not in required_skills:
                required_skills.append(skill.strip().lower())

        # Calculate and return match score
        match_score = 0
        for skill in required_skills:
            if skill in student_skills:
                match_score += 1

        return (match_score / len(required_skills)) * 100


student = StudentProfile(input().split(","))
job = JobDescription(input().split(","))

calculator = MatchScoreCalculator(student, job)
print(calculator.analyze())