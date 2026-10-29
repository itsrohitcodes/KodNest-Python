# Generate a Sequence of Values on Demand

def generate_points(levels):
    # Write your code here
    points = 10
    for i in range(levels):
        yield points
        points *= 2

levels = int(input())
k = int(input())

points = generate_points (levels)
selected = []

for _ in range(k):
    value = next (points, None)
    if value is None:
        break
    selected. append (value)

if selected:
    print(*selected)
else:
    print("No points")