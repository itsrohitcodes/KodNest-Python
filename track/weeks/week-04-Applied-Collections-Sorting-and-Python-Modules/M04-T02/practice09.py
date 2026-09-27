# Create a set of unique first letters

def create_unique_first_letters(words):
    # Write your set comprehension here
    word = {word[0] for word in words}

    return word


n = int(input())
words = input().split()

unique_letters = create_unique_first_letters(words)

alphabetical_letters = [
    letter
    for letter in "abcdefghijklmnopqrstuvwxyz"
    if letter in unique_letters
]

print(*alphabetical_letters)