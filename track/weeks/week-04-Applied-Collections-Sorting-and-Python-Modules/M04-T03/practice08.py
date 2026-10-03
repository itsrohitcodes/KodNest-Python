# Rank Job Applications Using Score and Name

n = int(input())
applications = []

for _ in range(n):
    name, score = input().split()
    applications.append((name, int(score)))

# Write your code here
sorted_applications = sorted(applications, key = lambda i : (-i[1], i[0]))

for name, score in sorted_applications:
    print(name, score)