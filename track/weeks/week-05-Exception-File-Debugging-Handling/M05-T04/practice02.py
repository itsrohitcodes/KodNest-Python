# Fix Errors in Match Score Calculation

matched_skills = int(input())
required_skills = int(input())

match_score = (matched_skills / required_skills) * 100

print(f"{match_score}%")