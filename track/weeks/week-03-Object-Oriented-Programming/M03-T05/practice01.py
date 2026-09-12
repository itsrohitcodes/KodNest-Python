# Count Matching Skills using list and loops

def count_matching_skills(student_skills, required_skills):
    count = 0

    # Write your code here
    for skill in required_skills:
        if skill in student_skills:
            count += 1

    return count


student_skills = input().split(",")
required_skills = input().split(",")

print(count_matching_skills(student_skills, required_skills))