# Sort Transaction Amounts Without Changing the Original List

n = int(input())
transactions = list(map(int, input().split()))

# Write your code here
asc = sorted(transactions)

print(*asc)
print(*transactions)