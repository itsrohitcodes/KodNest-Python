# Display Products Available at Every Store Branch

n = int(input())
branches = []

for _ in range(n):
    data = input().split()
    branch_name = data[0]
    products = data[1:]

    branches.append({
        "branch": branch_name,
        "products": products
    })

# Write your code here
for branch in branches:
    branch_name = branch["branch"]
    products = branch["products"]

    for product in products:
        print(f"{branch_name}: {product}")
