# Convert a number sign checker into function

# defining the function to check the sign of a number
def check_sign(number):
    # checking the sign of the number
    if number > 0:
        value = "Positive"
    elif number < 0:
        value = "Negative"
    else:
        value = "Zero"
    return value

# reading the input
number = int(input())

# calling the function and storing the result
result = check_sign(number)

# printing the result
print(result)