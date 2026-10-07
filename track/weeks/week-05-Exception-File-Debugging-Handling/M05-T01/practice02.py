# Safely Read Student Skill Count

# Write your code here
skill_count = input()

try:
    skill_count = int(skill_count)
    print("Skill Count:", skill_count)

except ValueError:
    print("Invalid skill count")