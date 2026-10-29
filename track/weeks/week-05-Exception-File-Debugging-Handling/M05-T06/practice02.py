# Process Values Using next()

n = int(input())
quantities = list(map(int, input().split()))
k = int(input())

# Write your code here
iter_quantities = iter(quantities)

total = 0

for i in range(k):
    quantity = next(iter_quantities, None)
    if quantity is None:
        break

    total += quantity

print(total)