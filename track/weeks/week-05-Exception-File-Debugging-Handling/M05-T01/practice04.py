# Safely Read Job Skill Count

# Write your code here
require_skill = input()

try:
    require_skill = int(require_skill)
    print("Required Skill Count:", require_skill)

except ValueError:
    print("Invalid skill count")