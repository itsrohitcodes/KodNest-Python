# Convert JSON Text back to Python Data

import json

# Write your code here
data = input()

product = json.loads(data)

print(product["name"])
print(product["price"])