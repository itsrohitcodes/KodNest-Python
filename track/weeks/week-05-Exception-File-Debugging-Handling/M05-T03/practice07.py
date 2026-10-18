# Process Values from File Data

# Write your code here
n = int(input())
prices = []

for i in range(n):
    price = int(input())
    prices.append(price)

highest = max(prices)

print(highest)