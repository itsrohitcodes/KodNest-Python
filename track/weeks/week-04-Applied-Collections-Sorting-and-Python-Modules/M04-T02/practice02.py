# Calculate Discounted Prices using List Comprehension

def calculate_discounted_prices(prices, discount_percentage):
    # Write your list comprehension here
    discounted_price = [price - (price * discount_percentage / 100) for price in prices]

    return discounted_price


n = int(input())
prices = list(map(int, input().split()))
discount_percentage = int(input())

discounted_prices = calculate_discounted_prices(
    prices, discount_percentage
)

print(*discounted_prices)