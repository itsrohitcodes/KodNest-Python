# Sort City Names Alphabetically

n = int(input())
cities = []

for _ in range(n):
    cities.append(input().strip())

# Write your code here
sort_cities = sorted(cities)

for city in sort_cities:
    print(city)