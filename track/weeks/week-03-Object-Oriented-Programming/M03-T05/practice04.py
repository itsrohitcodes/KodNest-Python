# Build a Complete Match Score Calculator

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
        # Write your code here
        student_skills = []
        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

        required_skills = []
        for skill in job.required_skills:
            if skill.strip() != "":
                required_skills.append(skill.strip().lower())

        matched_skills = []
        for skill in required_skills:
            if skill in student_skills:
                matched_skills.append(skill)

        if required_skills == 0:
            return 0
        else:
            return len(matched_skills) / len(required_skills) * 100


student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)
calculator = MatchScoreCalculator(student, job)

print(calculator.analyze())