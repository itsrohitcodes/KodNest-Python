# Analyze a list of scores

# Number of scores to read
n = int(input())
scores = []

# Read and store all scores
for i in range(n):
    score = int(input())
    scores.append(score)

# Score to search for
search_score = int(input())

# Display the highest, lowest and total scores
highest = max(scores)
lowest = min(scores)
total = sum(scores)

print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Total Score: {total}")

# Display whether search_score is present
status = "Not Found"
for i in scores:
    if i == search_score:
        status = "Found"

print(f"Search Result: {status}")