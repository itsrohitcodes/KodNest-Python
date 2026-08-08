# Calculate total using while loop

# Read the value of n
n = int(input())

# Initialize the counter and total
counter = 1
total = 0

# Calculate the total using a while loop
while counter <= n:
    total = total + counter
    counter = counter + 1
    
# Display the total
print(f"Total: {total}")