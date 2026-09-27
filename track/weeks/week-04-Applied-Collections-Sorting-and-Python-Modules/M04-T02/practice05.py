# Convert Names to Uppercase using List Comprehension

def convert_to_uppercase(names):
    # Write your list comprehension here
    uppercase = [name.upper() for name in names]

    return uppercase


n = int(input())
names = input().split()

uppercase_names = convert_to_uppercase(names)
print(*uppercase_names)