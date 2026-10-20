# Fix and Test a Buggy Decision Engine

matched_skills = int(input())
required_skills = int(input())
student_experience = int(input())
required_experience = int(input())

match_score = matched_skills / required_skills * 100

if student_experience >= required_experience:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

print(f"Match Score: {match_score:.1f}%")
print("Eligibility:", eligibility)