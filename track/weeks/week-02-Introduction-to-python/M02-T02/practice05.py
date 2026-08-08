# Analyze multiple of three and search target number

# Read limit and target number
limit = int(input())
target = int(input())

# Initialize counter and total
count = 0
total = 0
found = False

# Examine every number from 1 to the limit
for i in range(1,limit+1):
    # Check if the number is a multiple of 3
    if i % 3 == 0:
        count = count + 1
        total = total + i
    if i == target:
        found = True
        break
# Check if target was found
# Convert boolean to string
if found == True:
    found = "Yes"
else:
    found = "No"
    
# Display the count, total and search result
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Target Found: {found}")