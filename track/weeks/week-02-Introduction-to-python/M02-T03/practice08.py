# Process a student skill record

# Reading and storing five skills
skills = []
for i in range(5):
    skill = input()
    skills.append(skill)

# Convert the list into a tuple
skill_record = tuple(skills)

# Create the required slices

# Display all required results
print(f"Skill Record: {skill_record}")
print(f"First Three: {skill_record[:3]}")
print(f"Last Two: {skill_record[-2:]}")
print(f"Alternate Skills: {skill_record[::2]}")
print(f"Reversed Skills: {skill_record[::-1]}")