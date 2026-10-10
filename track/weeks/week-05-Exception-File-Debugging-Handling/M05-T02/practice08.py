# Validate Employee Working Hours

hours = int(input())

# Write your code here
try:
    if hours < 0 or hours > 12:
        raise ValueError("Working hours must be between 0 and 12")

    print("Valid working hours")

except ValueError as e:
    print(e)