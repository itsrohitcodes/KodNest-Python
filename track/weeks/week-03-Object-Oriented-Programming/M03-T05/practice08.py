# Analyze one student against one job

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
        # Complete this method
        student_skills = []
        for skill in self.student.skills:
            student_skills.append(skill.strip().lower())

        match_score = 0
        for skill in self.job.required_skills:
            if skill.strip().lower() in student_skills:
                match_score += 1

        return match_score / len(self.job.required_skills) * 100


class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        # Complete this method
        student_skills = []
        for skill in self.student.skills:
            student_skills.append(skill.strip().lower())

        missing_skills = []
        for skill in self.job.required_skills:
            if skill.strip().lower() not in student_skills:
                missing_skills.append(skill.strip())

        return missing_skills


student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)

score_calculator = MatchScoreCalculator(student, job)
missing_detector = MissingSkillDetector(student, job)

score = score_calculator.analyze()
missing_skills = missing_detector.analyze()

print(score)

if len(missing_skills) == 0:
    print("None")
else:
    print(", ".join(missing_skills))