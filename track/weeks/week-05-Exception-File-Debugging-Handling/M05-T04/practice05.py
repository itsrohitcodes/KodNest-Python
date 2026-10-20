# Debug Incorrect Match Score Calculation

required_skills = input().split(", ")
student_skills = input().split(", ")

matched_count = 0

for skill in required_skills:
    if skill in student_skills:
        matched_count += 1

match_score = matched_count / len(required_skills) * 100
print(f"Match Score: {match_score :. 1f}%")