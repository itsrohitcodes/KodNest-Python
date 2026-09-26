# Group Products according to thier Category

def group_products(products):
    products_by_category = {}

    # Write your grouping logic here
    for product_name, category in products:
        if category not in products_by_category:
            products_by_category[category] = []
        products_by_category[category].append(product_name)

    return products_by_category


n = int(input())
products = []

for _ in range(n):
    product_name, category = input().split()
    products.append((product_name, category))

products_by_category = group_products(products)

for category, product_names in products_by_category.items():
    print(category + ": " + " ".join(product_names))