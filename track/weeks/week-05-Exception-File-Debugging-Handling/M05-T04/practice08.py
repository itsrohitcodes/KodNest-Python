# Debug Preparation Plan Generation

required_skills = input().split(", ")
student_skills = input().split(", ")

plan = []

for skill in required_skills:
    if skill not in student_skills:
        plan.append(skill)

print("Preparation Plan:")
if plan:
    for i, skill in enumerate(plan, start=1):
        print(f"{i}. Learn {skill}")
else:
    print("No new skills needed")