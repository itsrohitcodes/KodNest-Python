# Sort Words According to Their Length

n = int(input())
words = input().split()

# Write your code here
sorted_words = sorted(words, key = lambda i : len(i))

print(*sorted_words)