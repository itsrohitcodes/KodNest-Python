# Calculate a Match Percentage Safely

def calculate_match_percentage(required_skills, matching_skills):
    # Write your code here
    if required_skills == 0:
        return 0
    else:
        return matching_skills / required_skills * 100


required_skills = int(input())
matching_skills = int(input())

print(calculate_match_percentage(required_skills, matching_skills))