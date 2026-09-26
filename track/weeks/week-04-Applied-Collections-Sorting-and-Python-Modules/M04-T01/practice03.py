# Check Product Availability using a Lookup Dictionary

def check_availability(inventory, product_code):
    # Write your dictionary lookup logic here
    if product_code not in inventory:
        return "Product not found"

    quantity = inventory[product_code]

    if quantity == 0:
        return "Out of stock"
    else:
        return f"Available: {quantity}"


inventory = {
    "P101": 12,
    "P102": 0,
    "P103": 7,
    "P104": 3
}

product_code = input()
print(check_availability(inventory, product_code))