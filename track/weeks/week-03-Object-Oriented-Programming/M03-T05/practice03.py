# Normalize Skill Before Comparison

def count_matches(student_skills, required_skills):
    # Write your code here
    student = []
    for skill in student_skills:
        student.append(skill.strip().lower())

    required = []
    for skill in required_skills:
        required.append(skill.strip().lower())

    matched = []
    match_count = 0
    for skill in required:
        if skill in student:
            matched.append(skill)
            match_count += 1

    return match_count

student_skills = input().split(",")
required_skills = input().split(",")

print(count_matches(student_skills, required_skills))