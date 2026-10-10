# Validate Account Balance

balance = int(input())

# Write your code here
try:
    if balance < 0:
        raise ValueError

    print("Valid balance")

except:
    print("Invalid balance")