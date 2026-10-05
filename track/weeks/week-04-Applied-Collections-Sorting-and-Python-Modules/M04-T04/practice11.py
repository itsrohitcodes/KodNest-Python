# Find the Most Frequently Required Skills

from collections import Counter

skills = input().split()

# Write your code here
skill_count = Counter(skills)

common_skill = skill_count.most_common(1)

for skill, count in common_skill:
    print(f"{skill}: {count}")