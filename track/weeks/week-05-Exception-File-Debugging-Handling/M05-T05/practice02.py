# Convert Strings to Uppercase

def to_uppercase(string):
    # TODO: Implement logic to convert string to uppercase
    return string. upper()

# TODO: Use map() to convert user_strings to uppercase
user_strings = list(map(str, input().split()))
# List of strings for conversion

upper_strings = list(map(to_uppercase, user_strings))

print(upper_strings)