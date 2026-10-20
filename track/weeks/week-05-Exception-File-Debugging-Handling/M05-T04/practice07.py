# Debug Missing Skill Detection

required_skills = input().split(", ")
student_skills = input().split(", ")

missing = []

for skill in required_skills:
    if skill not in student_skills:
        missing.append(skill)

if missing:
    print("Missing Skills: " + ", ".join(missing))
else:
    print("Missing Skills: None")