# Add an Analysis Method to Manager

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

        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

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
        missing_skills = []

        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

        for skill in self.job.required_skills:
            normalized_skill = skill.strip().lower()

            if normalized_skill != "" and normalized_skill not in student_skills:
                missing_skills.append(skill.strip())

        return missing_skills


class Manager:
    def analyze(self, student, job):
        # Write your code here
        score_calculator = MatchScoreCalculator(student, job)
        missing_detector = MissingSkillDetector(student, job)

        score = score_calculator.analyze()
        missing = missing_detector.analyze()

        return score, missing


student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)
manager = Manager()

score, missing_skills = manager.analyze(student, job)

print(score)

if len(missing_skills) == 0:
    print("None")
else:
    print(", ".join(missing_skills))