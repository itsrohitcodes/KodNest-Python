# Handle Multiple Job Input Errors

requirements = ["Python", "SQL", "Git", "REST API"]

# Write your code here
try:
    position = int(input())

    print(requirements[position])

except ValueError:
    print("Invalid position")

except IndexError:
    print("Requirement not found")