# Handle Multiple Student Profile Input Errors

skills = ["Python", "SQL", "Git", "HTML"]

# Write your code here
try:
    skill_position = input()
    skill_position = int(skill_position)
    print(skills[skill_position])

except ValueError:
    print("Invalid position")
    
except IndexError:
    print("Skill not found")    