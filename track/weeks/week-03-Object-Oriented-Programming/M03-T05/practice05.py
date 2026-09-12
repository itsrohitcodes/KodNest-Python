# Identify Missing Skills

def find_missing_skills(student_skills, required_skills):
    skills = []
    for skill in student_skills:
        skills.append(skill.strip().lower())

    missing_skills = []
    for skill in required_skills:
        if skill.strip().lower() not in skills:
            missing_skills.append(skill.strip())

    return missing_skills


n = int(input())
student_skills = input().split(",") if n > 0 else []

m = int(input())
required_skills = input().split(",") if m > 0 else []

result = find_missing_skills(student_skills, required_skills)

if result:
    print(", ".join(result))
else:
    print("No Missing Skills")