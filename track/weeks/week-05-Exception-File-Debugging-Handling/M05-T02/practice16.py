# Create an Exception for Excess Login Attempts

class LoginLimitError(Exception):
    pass

attempts = int(input())

# Write your code here
try:
    if attempts > 3:
        raise LoginLimitError("Login attempt limit exceeded")
        
    print("Login attempts allowed")
    
except LoginLimitError as e:
    print(e)