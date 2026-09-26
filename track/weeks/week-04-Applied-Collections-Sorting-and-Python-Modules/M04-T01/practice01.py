# Find product details using a product code

def find_product(products, product_code):
    # Write your dictionary lookup logic here
    return products.get(product_code)


products = {
    "P101": {"name": "Keyboard", "price": 1200},
    "P102": {"name": "Mouse", "price": 600},
    "P103": {"name": "Monitor", "price": 8500},
    "P104": {"name": "Headphones", "price": 1500}
}


product_code = input()
product = find_product(products, product_code)

if product is None:
    print("Product not found")
else:
    print(product["name"])
    print(product["price"])