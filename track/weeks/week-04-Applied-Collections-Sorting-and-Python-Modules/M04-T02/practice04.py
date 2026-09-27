# Convert Temperatures using List Comprehension

def convert_to_fahrenheit(celsius_temperatures):
    # Write your list comprehension here
    fahrenheit = [(celsius * 9/5) + 32 for celsius in celsius_temperatures]

    return fahrenheit


n = int(input())
celsius_temperatures = list(map(int, input().split()))

fahrenheit_temperatures = convert_to_fahrenheit(
    celsius_temperatures
)

print(*fahrenheit_temperatures)