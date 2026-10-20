# Correct and Verify Decision Engine Results

required_skills = input().split(", ")
student_skills = input().split(", ")
student_experience = int(input())
required_experience = int(input())

all_skills_matched = all(skill in student_skills for skill in required_skills)
experience_ok = student_experience >= required_experience

if all_skills_matched:
    print("Skill Status: Complete")
else:
    print("Skill Status: Incomplete")

if experience_ok:
    print("Experience Status: Eligible")
else:
    print("Experience Status: Not Eligible")

if all_skills_matched and experience_ok:
    print("Decision: Ready")
else:
    print("Decision: Not Ready")