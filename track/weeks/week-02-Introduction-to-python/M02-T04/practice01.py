# Build a simple calculator function

# defining the function to calculate the result
def calculate(first_number, second_number, operator):
    # Write your code here
    if operator == "+":
        return first_number + second_number 
    elif operator == "-":
        return first_number - second_number 
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    else:
        return None

# reading the inputs
first_number = int(input())
second_number = int(input())
operator = input().strip()

# calling the function and storing the result
result = calculate(first_number, second_number, operator)

# printing the result
print(result)