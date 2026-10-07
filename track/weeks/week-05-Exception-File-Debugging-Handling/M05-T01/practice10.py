# Complete Student Match Processing Safely

# Write your code here
matched_skills = input()
required_skills = input()

try:
    matched_skills = int(matched_skills)
    required_skills = int(required_skills)

    match_percentage = (matched_skills / required_skills) * 100

except ValueError:
    print("Invalid skill count")

except ZeroDivisionError:
    print("Required skills cannot be zero")

else:
    print("Match Percentage:", match_percentage)

finally:
    print("Match processing complete")