# Store Products Inside Invertory Categories

n = int(input())
inventory = {}

for _ in range(n):
    category, product_count = input().split()
    product_count = int(product_count)

    products = input().split()

    # Write your code here
    inventory[category] = products

print(inventory)