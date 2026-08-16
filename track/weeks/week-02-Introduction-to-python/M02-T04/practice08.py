# Track unique workshop registrations using a set

# Read the number of registration entries 
n = int(input())

# Create an empty set to store unique student IDs 
registrations = set()

# Read and store the student IDs 
for _ in range(n):
    student_id = input().strip()

    # TODO: Add the student ID to the set 
    registrations.add(student_id)

# Read the student ID to search 
search_id = input().strip()

# TODO: Calculate the number of unique registrations 
unique_count = len(set(registrations))

# TODO: Calculate the number of duplicate entries 
duplicate_count = n - len(set(registrations))

# Print the counts
print(f"Unique registrations: {unique_count}") 
print(f"Duplicate entries: {duplicate_count}")

# TODO: Check whether search_id exists in registrations
if search_id in registrations: 
    print("Registered")
else:
    print("Not Registered")