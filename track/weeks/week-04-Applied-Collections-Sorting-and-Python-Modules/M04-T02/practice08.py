# Build a Word-Length Dictionary

def build_word_length_dictionary(words):
    # Write your dictionary comprehension here
    res = {i:len(i) for i in words}

    return res


n = int(input())
words = input().split()

word_lengths = build_word_length_dictionary(words)

for word, length in word_lengths.items():
    print(word, length)