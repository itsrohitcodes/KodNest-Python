# Create a set of unique word lengths

def create_unique_lengths(words):
    # Write your set comprehension here
    word = {len(i) for i in words}

    return word


n = int(input())
words = input().split()

unique_lengths = create_unique_lengths(words)

ordered_lengths = [
    length
    for length in range(1, 21)
    if length in unique_lengths
]

print(*ordered_lengths)