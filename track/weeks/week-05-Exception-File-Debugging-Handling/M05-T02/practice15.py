# Create an Exception for Invalid Score

class InvalidScoreError(Exception):
    pass

score = int(input())

# Write your code here
try:
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")
        
    print("Valid score")
    
except InvalidScoreError as e:
    print(e)