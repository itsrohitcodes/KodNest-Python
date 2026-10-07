# Handle Student Skill Processing Errors

# Write your code here
try:
    matched_skills = int(input())
    required_skills = int(input())

    match_percentage = (matched_skills / required_skills) * 100

    print("Match Percentage:", match_percentage)

except ValueError:
    print("Invalid skill count")

except ZeroDivisionError:
    print("Required skills cannot be zero")