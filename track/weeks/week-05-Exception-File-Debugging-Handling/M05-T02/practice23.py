# Handle Invalid Employee Working Hours

class InvalidWorkingHoursError(Exception):
    pass

hours = int(input())

# Write your code here
try:
    if hours <= 0 or hours > 12:
        raise InvalidWorkingHoursError("Working hours must be between 1 and 12")

    print("Working hours accepted")

except InvalidWorkingHoursError as e:
    print(e)