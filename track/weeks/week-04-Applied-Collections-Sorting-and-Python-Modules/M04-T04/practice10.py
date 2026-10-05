# Count Votes Received by Every Candidates

from collections import Counter

votes = input().split()

# Write your code here
counted_vote = Counter(votes)

for name, count in counted_vote.items():
    print(f"{name}: {count}")