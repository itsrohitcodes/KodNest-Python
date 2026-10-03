# Sort Products According to Price and Product Name

n = int(input())
products = []

for _ in range(n):
    product_name, price = input().split()
    products.append((product_name, int(price)))

# Write your code here
sorted_products = sorted(products, key = lambda i : (i[1], i[0]))

for name, price in sorted_products:
    print(name, price)