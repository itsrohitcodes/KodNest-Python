# Display a number sequence and characters of a word
# Read the number and word
number = int(input())
word = input()

# Print the number sequence
print("Numbers:")
for i in range(1, number+1): 
    print(i)

# Print the characters
print("Characters:")
for i in word:
    print(i)