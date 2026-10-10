# Handle Student Eligibility Validation

class EligibilityError(Exception):
    pass

attendance = int(input())

# Write your code here
try:
    if attendance < 75:
        raise EligibilityError("Attendance must be at least 75")
        
    print("Eligible for training")
    
except EligibilityError as e:
    print(e)