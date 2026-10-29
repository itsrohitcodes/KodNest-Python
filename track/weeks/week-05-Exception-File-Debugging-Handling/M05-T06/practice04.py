# Process Product Prices Using an Iterator

n = int(input())
prices = list(map(int, input().split()))
k = int(input())

# Write your code here
iter_prices = iter(prices)

total_price = 0

for i in range(k):
    price = next(iter_prices, None)
    if price is None:
        break

    total_price += price

print(total_price)