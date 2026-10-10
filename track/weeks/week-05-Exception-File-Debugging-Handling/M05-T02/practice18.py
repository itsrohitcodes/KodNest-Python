# Create an Exception for Invalid Salary

class InvalidSalaryError(Exception):
    pass

salary = int(input())

# Write your code here
try:
    if salary <= 0:
        raise InvalidSalaryError("Salary must be greater than 0")
        
    print("Valid salary")
    
except InvalidSalaryError as e:
    print(e)