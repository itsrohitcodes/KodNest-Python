# Build the Complete Missing Skill Detector

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


class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        # Write your code here
        student_skills = []
        for skill in self.student.skills:
            student_skills.append(skill.strip().lower())

        require_skills = []
        for skill in self.job.required_skills:
            require_skills.append(skill.strip().lower())

        missing_skills = []
        for skill in require_skills:
            if skill not in student_skills:
                missing_skills.append(skill)

        return missing_skills


student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)
detector = MissingSkillDetector(student, job)

print(detector.analyze())