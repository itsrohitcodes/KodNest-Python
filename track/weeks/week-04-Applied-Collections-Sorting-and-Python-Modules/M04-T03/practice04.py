# Sort Recorded Temperatures in Descending Order

n = int(input())
temperatures = list(map(int, input().split()))

# Write your code here
desc = sorted(temperatures, reverse = True)

print(*desc)