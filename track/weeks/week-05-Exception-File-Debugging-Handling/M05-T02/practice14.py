# Create an Exception for Invalid Age

class InvalidAgeError(Exception):
    pass

age = int(input())

# Write your code here
try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
        
    print("Eligible")
    
except InvalidAgeError as e:
    print(e)