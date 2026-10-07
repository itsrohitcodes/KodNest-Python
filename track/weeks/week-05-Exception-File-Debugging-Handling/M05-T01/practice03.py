# Safely Read Job Experience Requirement

# Write your code here
experience = input()

try:
    experience = int(experience)
    print("Required Experience:", experience)

except ValueError:
    print("Invalid experience requirement")