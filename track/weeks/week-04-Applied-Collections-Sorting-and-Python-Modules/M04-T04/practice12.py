# Find the Most Common Customer Support Issues

from collections import Counter

issues = input().split()

# Write your code here
issues_count = Counter(issues)

most_issues = issues_count.most_common(2)

for issue, count in most_issues:
    print(f"{issue}: {count}")