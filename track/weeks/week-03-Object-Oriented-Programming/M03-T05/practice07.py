# Run Both Analyzers Polymorphically 

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

        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

        required_skills = []

        for skill in self.job.required_skills:
            if skill.strip() != "":
                required_skills.append(skill.strip().lower())

        if len(required_skills) == 0:
            return 0

        match_count = 0

        for skill in required_skills:
            if skill in student_skills:
                match_count += 1

        return (match_count / len(required_skills)) * 100


class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        student_skills = []

        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

        missing_skills = []

        for skill in self.job.required_skills:
            normalized_skill = skill.strip().lower()

            if normalized_skill != "" and normalized_skill not in student_skills:
                missing_skills.append(normalized_skill)

        return missing_skills


student = StudentProfile(input().split(","))
job = JobDescription(input().split(","))

# Write your code here
match_score = MatchScoreCalculator(student, job)
missing = MissingSkillDetector(student, job)

print(match_score.analyze())
print(missing.analyze())