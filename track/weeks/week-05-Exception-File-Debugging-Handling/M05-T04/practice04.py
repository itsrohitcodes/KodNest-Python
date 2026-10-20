# Fix Errors in Skill Processing

required_skills = input().split(", ")
student_skills = input().split(", ")

missing_skills = []

for skill in required_skills:
    if skill not in student_skills:
        missing_skills.append(skill)

if missing_skills:
    print("Missing Skills: " + ", ".join(missing_skills))
else:
    print("Missing Skills: None")