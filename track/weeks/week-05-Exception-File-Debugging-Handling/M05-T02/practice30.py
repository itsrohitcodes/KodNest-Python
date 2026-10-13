# Validate Course Enrollment

class InvalidAgeError(Exception):
    pass

class NoSeatsAvailableError(Exception):
    pass

age = int(input())
seats = int(input())

# Write your code here
try:
    if age < 16:
        raise InvalidAgeError("Age must be at least 16")

    if seats <= 0:
        raise NoSeatsAvailableError("No seats available")

    print("Enrollment successful")

except InvalidAgeError as e:
    print(e)

except NoSeatsAvailableError as e:
    print(e)