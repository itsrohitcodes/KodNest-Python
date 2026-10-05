# Count Repeated Words using Counter

from collections import Counter

words = input().split()

# Write your code here
words_count = Counter(words)

for word, count in words_count.items():
    print(f"{word}: {count}")