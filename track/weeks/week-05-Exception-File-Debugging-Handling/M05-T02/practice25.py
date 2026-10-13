# Apply Exception Validation to User Registration

class InvalidAgeError(Exception):
    pass

class WeakPasswordError(Exception):
    pass

age = int(input())
password = input()

# Write your code here
try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    if len(password) < 6:
        raise WeakPasswordError("Password must contain at least 6 characters")

    print("Registration successful")

except InvalidAgeError as e:
    print(e)

except WeakPasswordError as e:
    print(e)