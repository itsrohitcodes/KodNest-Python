# Handle Invalid Course Registration

class InvalidRegistrationError(Exception):
    pass

courses = int(input())

# Write your code here
try:
    if courses <= 0 or courses > 5:
        raise InvalidRegistrationError("You can register for 1 to 5 courses")
        
    print("Registration successful")

except InvalidRegistrationError as e:
    print(e)